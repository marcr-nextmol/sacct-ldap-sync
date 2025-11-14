import itertools
import subprocess
import ldaplib
from SlurmAccountManagerV41 import SlurmAccountManagerV41, AssociationExistsError
import os
import yaml
import sys
import logging
from typing import List, Dict, Tuple, Optional, Any

# Configure logging at module level
logger = logging.getLogger(__name__)
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

DEFAULT_EXCEPTIONS = ["easybuild", "root"]
DEFAULT_ORGANIZATION = "nextmol"

def gen_token() -> Optional[str]:
    """
    Generates a Slurm JSON Web Token (JWT) by executing the 'scontrol token' command.
    
    Returns:
        str or None: The generated Slurm JWT string, or None if generation fails.
    """
    try:
        result = subprocess.run(
            ['scontrol', 'token', 'lifespan=9999'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        for line in result.stdout.splitlines():
            if line.startswith('SLURM_JWT='):
                return line.replace('SLURM_JWT=', '')
        
        logger.warning("'SLURM_JWT=' not found in scontrol token output. ERROR: %s", 
                      result.stderr.strip())
        
    except subprocess.CalledProcessError as e:
        logger.error("Error executing scontrol command: %s\nStdout: %s\nStderr: %s", 
                    e, e.stdout, e.stderr)
    except FileNotFoundError:
        logger.error("'scontrol' command not found. Make sure Slurm is installed and in your PATH.")
    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
    
    return None

def _get_user_groups(ldap: Any, username: str, accounts_exception_list: List[str], 
                    extra_associations: Dict[str, List[str]]) -> List[str]:
    """Helper function to get user groups with exceptions and extra associations applied."""
    groups = {group for group, _ in ldap.get_all_groups_from_user(username)}
    groups -= set(accounts_exception_list)
    
    if extra_associations and username in extra_associations:
        groups.update(extra_associations[username])
    
    return [g for g in groups if g is not None]

def _ensure_string_param(param: Any, param_name: str) -> str:
    """Ensure parameter is a string, converting lists if necessary."""
    if isinstance(param, list):
        if len(param) == 1:
            return str(param[0])
        else:
            logger.warning("Parameter %s is a list with multiple values: %s. Using first value.", 
                          param_name, param)
            return str(param[0])
    return str(param)

def _handle_slurm_api_error(e: Exception, operation: str, details: str = "") -> bool:
    """
    Handle Slurm API errors, specifically ignoring 'data not changed' warnings.
    
    Returns:
        bool: True if the error is non-critical and can be ignored, False otherwise
    """
    error_str = str(e)
    
    if "Data has not changed" in error_str or "rc[1900]" in error_str:
        logger.debug("Slurm API non-critical warning for %s: %s", operation, error_str)
        return True  
        
    if "AssociationExistsError" in error_str or "already exists" in error_str.lower():
        logger.debug("Association already exists for %s: %s", operation, error_str)
        return True  #
        
    logger.error("Slurm API error during %s: %s. Details: %s", operation, error_str, details)
    return False

def create_slurm_association(ldap: Any, slurm: Any, user_exception_list: List[str] = None,
                            accounts_exception_list: List[str] = None, 
                            extra_association_list: List[Dict] = None,
                            organization: str = DEFAULT_ORGANIZATION) -> None:
    """
    Synchronizes user group memberships from LDAP to Slurm associations.

    Args:
        ldap: Initialized LDAP client object.
        slurm: Initialized Slurm API client object.
        user_exception_list: Usernames to exclude from synchronization.
        accounts_exception_list: LDAP groups (Slurm accounts) to ignore.
        extra_association_list: Extra account associations for users.
        organization: Default organization for new Slurm accounts.
    """
    if user_exception_list is None:
        user_exception_list = ["None"]
    if accounts_exception_list is None:
        accounts_exception_list = ["None"]
    if extra_association_list is None:
        extra_association_list = []

    try:
        users = ldap.get_users_list()
        user_list = [user[0] for user in users]
        clean_userlist = set(user_list) - set(user_exception_list)
        extra_associations = {}
        for item in extra_association_list:
            user = _ensure_string_param(item.get('user'), 'user')
            accounts = item.get('accounts', [])
            if isinstance(accounts, str):
                accounts = [accounts]
            extra_associations.setdefault(user, []).extend(accounts)
        
        existing_associations = set(slurm.get_associations_list())
        
        for username in clean_userlist:
            groups = _get_user_groups(ldap, username, accounts_exception_list, extra_associations)
            safe_username = _ensure_string_param(username, 'username')

            if not groups:
                continue
                
            logger.info("Processing user %s with groups %s", username, groups)
            
            for group in groups:
                existing_associations = set(slurm.get_associations_list())
                association_key = (username, group)
                safe_group = _ensure_string_param(group, 'group')   

                if association_key not in existing_associations:
                    logger.info("Creating Slurm association for user %s and account %s", username, group)   
                    

                    # Create account association           
                    slurm_accounts=[account for account,_ in slurm.get_accounts_list()]
                    if safe_group not in slurm_accounts:
                        try:
                            slurm_account_association = slurm.post_account_association(safe_username, [safe_group])
                            logger.debug("Slurm account association creation response: %s", 
                                slurm_account_association)
                        except AssociationExistsError as e:
                            logger.debug("Association account already exists: %s", e)
                    # Create user association
                    try:
                       
                        slurm_user_association = slurm.post_user_association(safe_username, [safe_group])
                        logger.debug("Slurm association (%s) creation response: %s", 
                                    association_key, slurm_user_association)
                    except AssociationExistsError as e:
                        logger.debug("Association user already exists: %s", e)
                        

                    except Exception as e:
                        if not _handle_slurm_api_error(e, f"association creation for {association_key}"):
                            raise
                    
    except Exception as e:
        logger.error("An error occurred during association creation: %s", e)


def create_users(ldap: Any, slurm: Any, admin_users: list[str], exception_list: List[str] = None) -> None:  
    """
    Creates Slurm users based on LDAP users, excluding specified exceptions.
    """
    if exception_list is None:
        exception_list = DEFAULT_EXCEPTIONS.copy()
    try:
        users = ldap.get_users_list()
        user_list = [user[0] for user in users]
        clean_userlist = set(user_list) - set(exception_list)
        admin_level=False
        slurm_users = slurm.get_users_list()
        slurm_usernames = [user[0] for user in slurm_users]
        print(clean_userlist)
        for username in clean_userlist:
                admin_level="None"
                logger.info("Creating Slurm user %s", username)
                try:
                    if username in admin_users:
                        logger.info("Assigning admin privileges to user %s", username)
                        admin_level="Administrator"
                    safe_username = _ensure_string_param(username, 'username')
                    create_response = slurm.post_user(safe_username,admin_level=admin_level)
                    logger.debug("Slurm user creation response: %s", create_response)
                except Exception as e:
                    if not _handle_slurm_api_error(e, f"user creation for {username}"):
                        logger.error("Error creating user %s: %s", username, e)
                    
    except Exception as e:
        logger.error("An error occurred during user creation: %s", e)   

def delete_users(ldap: Any, slurm: Any, exception_list: List[str] = None) -> None:
    """
    Deletes users from Slurm who no longer exist in the LDAP directory.
    """
    if exception_list is None:
        exception_list = DEFAULT_EXCEPTIONS.copy()
    
    try:
        users = ldap.get_users_list()
        user_list = [user[0] for user in users]
        ldap_users_set = set(user_list) | set(exception_list)
        
        slurm_users = slurm.get_users_list()
        slurm_usernames = [user[0] for user in slurm_users]
        
        users_to_delete = set(slurm_usernames) - ldap_users_set
        
        logger.debug("Users to be deleted from Slurm: %s", users_to_delete)
        
        for username in users_to_delete:
            logger.info("Deleting Slurm user %s (not present in LDAP)", username)
            try:
                safe_username = _ensure_string_param(username, 'username')
                delete_response = slurm.delete_user(safe_username)
                logger.debug("Slurm user deletion response: %s", delete_response)
            except Exception as e:
                if not _handle_slurm_api_error(e, f"user deletion for {username}"):
                    logger.error("Error deleting user %s: %s", username, e)
            
    except Exception as e:
        logger.error("An error occurred during user deletion: %s", e)

def convert_association_dict_to_tuple(association_dict: List[Dict]) -> List[Tuple[str, str]]:
    """
    Converts a list of association dictionaries to a list of tuples.
    """
    associations = []
    for assoc in association_dict:
        user = _ensure_string_param(assoc.get("user"), "user")
        accounts = assoc.get("accounts", [])
        if isinstance(accounts, str):
            accounts = [accounts]
        for account in accounts:
            safe_account = _ensure_string_param(account, "account")
            associations.append((user, safe_account))
    return associations

def get_associations_list(slurm: Any) -> List[Tuple[str, str]]:
    """
    Get associations list from Slurm, filtering out empty usernames.
    """
    try:
        associations = slurm.get_associations_list()
        # Filter out associations with empty usernames
        return [(assoc.user, assoc.account) for assoc in associations if assoc.user != '']
    except Exception as e:
        logger.error("Error getting associations list: %s", e)
        return []

def delete_association(ldap: Any, slurm: Any, exception_assoc_list: List[Dict] = None,
                      exception_userlist: List[str] = None) -> None:
    """
    Deletes Slurm user-account associations for users no longer present in LDAP.
    """
    if exception_assoc_list is None:
        exception_assoc_list = []
    if exception_userlist is None:
        exception_userlist = DEFAULT_EXCEPTIONS.copy()
    
    try:
        users = ldap.get_users_list()
        user_list = [user[0] for user in users]
        
        exception_assoc_tuples = convert_association_dict_to_tuple(exception_assoc_list)
        logger.debug("exception associations:", exception_assoc_tuples)
        slurm_associations = set(slurm.get_associations_list()) 
        logger.debug("slurm associations:", slurm_associations)
        
    
        list_tuples_ldap=set(itertools.chain.from_iterable(list(map(ldap.get_tuple_user_info, user_list))+[exception_assoc_tuples]))

        logger.debug("ldap associations:", list_tuples_ldap)
        assoc_to_delete = list((slurm_associations) - (list_tuples_ldap))
        logger.debug("interseccion:", assoc_to_delete)


        for association in assoc_to_delete:
            for username, account in [association]:
                if username not in exception_userlist: 
                    logger.info(f"Deleting associations for user {association}")
                    slurm.delete_association(username, account)
        
    except Exception as e:
        logger.error("An error occurred during association deletion: %s", e)

def read_config(config_file: str) -> Optional[Dict[str, Any]]:
    """
    Reads a YAML configuration file and returns its content.
    """
    if not os.path.exists(config_file):
        logger.error("Configuration file not found at '%s'", config_file)
        return None
    
    try:
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        
        if not isinstance(config_data, dict):
            logger.error("YAML content in '%s' is not a valid dictionary", config_file)
            return None
            
        return config_data
        
    except yaml.YAMLError as e:
        logger.error("Invalid YAML format in '%s': %s", config_file, e)
        return None
    except Exception as e:
        logger.error("Unexpected error reading '%s': %s", config_file, e)
        return None

def main() -> int:
    """
    Main function to execute the LDAP and Slurm synchronization process.
    """
    config = read_config("config.yaml")
    
    if not config:
        logger.error("Failed to read configuration. Exiting.")
        return 1
    
    # Configure logging level
    log_level = logging.DEBUG if config.get("LoggingLevel") == "DEBUG" else logging.INFO
    logger.setLevel(log_level)
    logger.debug("Configuration: %s", config)
    
    try:
        # Initialize Slurm Account Manager
        jwt_token = config.get("SlurmJWTToken") or gen_token()
        api_url = config.get("SlurmAPIURL", "http://localhost:6820")
        
        slurm = SlurmAccountManagerV41(jwt_token=jwt_token, api_url=api_url)
        logger.debug("Using Slurm API URL: %s", api_url)
        
        # Initialize LDAP Client
        ldap = ldaplib.ldaplib(
            LdapServer=config.get("LdapServer", "ldap://localhost"),
            BaseDN=config.get("LdapBaseDN", "DC=nextmol,DC=local")
        )
        
        # Get configuration values with defaults
        no_ldap_users = config.get("NoLDAPUsersList", DEFAULT_EXCEPTIONS.copy())
        extra_associations = config.get("ExtraLDAPUserAssociations", [])
        api_url = config.get("SlurmAPIURL", "http://localhost:6820")
        
        if isinstance(no_ldap_users, str):
            no_ldap_users = [no_ldap_users]

        # Create Slurm users
        create_users(
            ldap, slurm,
            admin_users=config.get("AdminUsersList", []),
            exception_list=no_ldap_users
        )
        
        # Create Slurm associations
      #  create_slurm_association(
      #      ldap, slurm,
       #     user_exception_list=no_ldap_users,
        #    accounts_exception_list=no_ldap_users,
         #   extra_association_list=extra_associations,
          #  organization=config.get("DefaultOrganization", DEFAULT_ORGANIZATION)
       #)
        # Delete Slurm users not in LDAP        
        #delete_users(ldap, slurm, exception_list=no_ldap_users)
        # Delete Slurm associations not in LDAP
       # delete_association(ldap, slurm, 
                    #       exception_assoc_list=extra_associations,
                     #      exception_userlist=no_ldap_users)
        
        logger.info("LDAP-Slurm synchronization completed successfully")
        return 0
        
    except Exception as e:
        logger.error("Fatal error during synchronization: %s", e)
        return 1

if __name__ == "__main__":
    sys.exit(main())