import subprocess
import ldaplib
from SlurmAccountManagerV41 import SlurmAccountManagerV41,AssociationExistsError
import os, yaml, sys
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def gen_token():
    """
    Generates a Slurm JSON Web Token (JWT) by executing the 'scontrol token' command.

    This token is required for authenticating with the Slurm REST API.

    Returns:
        str or None: The generated Slurm JWT string (excluding 'SLURM_JWT='),
                     or None if the command fails or the token cannot be found.
    """
    c_access_token = None
    try:
        result = subprocess.run(
            ['scontrol', 'token', 'lifespan=9999'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout_str = result.stdout.decode('utf-8').strip()
        stderr_str = result.stderr.decode('utf-8').strip()

        token_line = next((line for line in stdout_str.splitlines() if line.startswith('SLURM_JWT=')), None)
        if token_line:
            c_access_token = token_line.replace('SLURM_JWT=', '')

        else:
            print(f"Warning: 'SLURM_JWT=' not found in scontrol token output.ERROR:{stderr_str}")

    except subprocess.CalledProcessError as e:
        print(f"Error executing scontrol command: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print("Error: 'scontrol' command not found. Make sure Slurm is installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        return c_access_token
    
    
def create_slurm_association(ldap,
                             slurm,
                             user_exception_list=["None"],
                             accouts_exception_list=["None"],
                             extra_association_list={},
                             organization="nextmol",
                             default_account="nextmol"):
    """
    Synchronizes user group memberships from LDAP to Slurm associations.

    It creates Slurm users and their associations with groups (Slurm accounts)
    based on the current LDAP configuration, respecting exception lists.

    Args:
        ldap (ldaplib.ldaplib): An initialized LDAP client object.
        slurm (SlurmAccountManagerV41.SlurmAccountManagerV41): An initialized Slurm API client object.
        user_exception_list (list): A list of usernames to exclude from synchronization.
        accouts_exception_list (list): A list of LDAP groups (Slurm accounts) to ignore.
        extra_association_list (dict): A dictionary mapping usernames to a list of extra
                                       Slurm accounts they should be associated with.
        organization (str): The default organization name for new Slurm accounts/associations.
        default_account (str): The default Slurm account (group) name (currently unused in the logic).
    
    Returns:
        None
    """
    try:
        users = ldap.get_users_list()
        user_list = list(map(lambda x: x[0], users))
        clean_userlist=list(set(user_list)-set(user_exception_list))   
        assoctlist=slurm.get_associations_list()
        for username in clean_userlist:
            groups=list(set([group for group,gid in ldap.get_all_groups_from_user(username)])-set(accouts_exception_list))
            print(f"Processing user {username} with groups {groups}")
            if groups:
                extra_association_dict = {}
                for item in extra_association_list:
                    extra_association_dict.setdefault(item['user'], []).append(item['account'])
                if username in extra_association_dict:
                    groups.append(extra_association_dict[username][0])
                    print(groups)
                logger.debug(f"User {username} has groups: {groups}")
                for group in groups:
                    if group is None:
                        continue
                    print(f"Processing group {group} for user {username}")
                    if (username,group) not in assoctlist:
                        try:
                            slurm_user_association=slurm.post_user_association(username,[group])
                            logger.debug(f"Slurm association ({username,group}) creation response: {slurm_user_association}")
                        except AssociationExistsError as e:
                            print(f"Slurm association: {e}")
                    if (username,group) not in assoctlist:
                        try:
                            print(f"Creating Slurm account association of user {username} with account {group}")
                            slurm_account_association=slurm.post_account_association(username,group)
                            logger.debug(f"Slurm account association creation response: {slurm_account_association}")  
                        except AssociationExistsError as e:
                            print(f"Slurm account association:{e}")
    except Exception as e:
        print(f"An error occurred during association creation: {e}")
    
    
def delete_users(ldap,slurm,excetionlist=["root","easybuild"]):
    """
    Deletes users from Slurm who no longer exist in the LDAP directory.

    Compares the current list of Slurm users against the list of active LDAP users
    and an exception list, deleting any user that is only in Slurm.

    Args:
        ldap (ldaplib.ldaplib): An initialized LDAP client object.
        slurm (SlurmAccountManagerV41.SlurmAccountManagerV41): An initialized Slurm API client object.
        excetionlist (list): A list of usernames that should NOT be deleted from Slurm,
                             even if they are not found in LDAP.
    
    Returns:
        None
    """
    users = ldap.get_users_list()
    user_list = list(map(lambda x: x[0], users))
    full_ldap_userlist= user_list+excetionlist
    logger.debug(f"Full LDAP user list: {full_ldap_userlist}")
    slurm_users=slurm.get_users_list()
    slurm_usernames=list(map(lambda x: x[0], slurm_users))
    logger.debug(f"Slurm user list: {slurm_usernames}")
    intersection = (set(slurm_usernames)-set(full_ldap_userlist))
    logger.debug(f"Users to be deleted from Slurm: {intersection}")
    for slurm_username in intersection:
            print(f"Deleting slurm user {slurm_username} as it is not present in LDAP")
            delete_response=slurm.delete_user(slurm_username)
            logger.debug(f"Slurm user deletion response: {delete_response}")

def convert_association_dic_to_tuple(association_dict:list) -> list:
    """
    Converts a dictionary of user-account associations into a list of tuples.

    Args:
        association_dict (dict): A dictionary where keys are usernames and values
                                 are lists of account names. 
    Returns:
        list: A list of tuples, each containing a (username, accountname) pair.
 """         
    return [(association["user"],association["account"]) for association in association_dict]

def delete_association(ldap,slurm,exception_assoc_list=[],excetpion_userlist=["root","easybuild"]):
    """
    Deletes Slurm user-account associations for users no longer present in LDAP.

    Compares the current list of Slurm associations against the list of active LDAP users
    and an exception list, deleting any association where the user is not found in LDAP.

    Args:
        ldap (ldaplib.ldaplib): An initialized LDAP client object.
        slurm (SlurmAccountManagerV41.SlurmAccountManagerV41): An initialized Slurm API client object.
        excetionlist (list): A list of usernames whose associations should NOT be deleted from Slurm,
                             even if they are not found in LDAP.
    """
    users = ldap.get_users_list()
    user_list = list(map(lambda x: x[0], users))
    tuple_exception_assoc_list= convert_association_dic_to_tuple(exception_assoc_list)
    slurm_associations=slurm.get_associations_list()+tuple_exception_assoc_list
    print(exception_assoc_list)
    print(tuple_exception_assoc_list)
    for user in user_list:
        ldap_list_association=[(association[0],association[1][0]) for association in ldap.get_tuple_user_info(user)]
        for ldap_assoc in ldap_list_association:
             if ldap_assoc[1] is None:
                ldap_assoc=(ldap_assoc[0],"nextmol")
             if ldap_assoc[0] in excetpion_userlist:
                continue
             if ldap_assoc not in slurm_associations:
                print(f"Deleting slurm association {ldap_assoc} as user {ldap_assoc[0]} is not present in LDAP")
                slurm.delete_association(ldap_assoc[0], ldap_assoc[1])
            
      
def read_config(configfile):
    """
    Reads a YAML configuration file and returns its content as a Python dictionary.

    Args:
        configfile (str): The full path to the YAML configuration file.

    Returns:
        dict or None: A dictionary containing the configuration data, or None if an 
                      error occurs (file not found, invalid YAML).
    """
    if not os.path.exists(configfile):
        print(f"Error: Configuration file not found at '{configfile}'")
        return None
    try:
        with open(configfile, 'r') as file:
            config_data = yaml.safe_load(file)
    
        if isinstance(config_data, dict):
            return config_data
        else:
            print(f"Error: YAML content in '{configfile}' is not a valid dictionary.")
            return None
            
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML format in '{configfile}'. Details: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading '{configfile}': {e}")
        return None

    

def main():
    """
    Main function to execute the LDAP and Slurm synchronization process.

    It reads configuration, initializes the LDAP and Slurm managers, and then
    calls the functions to create associations and delete stale users.
    
    Returns:
        None
    """
    exceptions=["easybuild","root"]
    config=read_config("config.yaml")
    
    if not config:
        print("Failed to read configuration. Exiting.")
        return 1
        
    if config.get("LoggingLevel","INFO")== "DEBUG":
        logger.setLevel(logging.DEBUG)
        logger.debug("Debugging is enabled.")
    else:
        logger.setLevel(logging.INFO)
        
    logger.debug(config)
    
    # Initialize Slurm Account Manager
    slurm=SlurmAccountManagerV41(
        jwt_token=config.get("SlurmJWTToken",gen_token()),
        api_url=config.get("SlurmAPIURL","http://localhost:6820"))
    logger.debug(f"Using Slurm API URL: {config.get("SlurmAPIURL","http://localhost:6820")}")
    
    # Initialize LDAP Client
    ldap = ldaplib.ldaplib(LdapServer=config.get("LdapServer","ldap://localhost"),
                           BaseDN=config.get("LdapBaseDN","DC=nextmol,DC=local"))
    
    # Create/Update associations
    create_slurm_association(ldap,slurm,
                             user_exception_list=config.get("NoLDAPUsersList",["none"]),
                             accouts_exception_list=config.get("NoLDAPUsersList",["none"]),
                             extra_association_list=config.get("ExtraLDAPUserAssociations",{}),
                             organization=config.get("DefaultOrganization","nextmol"))
    
    logger.debug(config.get("NoLDAPUsersList",exceptions))
    
    # Delete stale users
    delete_users(ldap,slurm, excetionlist=config.get("NoLDAPUsersList",exceptions))

    # Delete users from goups 
    delete_association(ldap,
                       slurm,
                       exception_assoc_list=config.get("ExtraLDAPUserAssociations",[]),
                       excetpion_userlist=config.get("NoLDAPUsersList",exceptions))


if __name__ == "__main__":
    main()