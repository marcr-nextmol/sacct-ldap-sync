import subprocess 
from ldap3 import Server, Connection, ALL, SUBTREE
from typing import List 

#Vustom classes or generated from an OpenAPI spec for SlurmDB
from models.v0_0_40_account import V0040Account 
from models.v0_0_40_user import V0040User
from models.v0_0_40_openapi_resp import V0040OpenapiResp
from slurm_rest_api.api.slurm_api import SlurmApi 
from slurm_rest_api.api.slurmdb_api import SlurmdbApi 
from slurm_rest_api.rest import ApiException
from slurm_rest_api.configuration import Configuration as Config 
from slurm_rest_api.api_client import ApiClient as Client 

# --- LDAP Utility Functions ---

def get_ldap_users_by_group():
    """
    Connects to the LDAP server and retrieves a dictionary of groups
    where keys are group names and values are lists of their member UIDs.
    Only retrieves entries with objectClass 'posixGroup'.
    """
    server = Server(LDAP_SERVER, get_info=ALL) # Initialize LDAP server connection
    conn = Connection(server, auto_bind=True) # Establish connection and bind automatically
    conn.search(
        search_base=BASE_DN, 
        search_filter='(objectClass=posixGroup)', # Filter for posixGroup objects
        search_scope=SUBTREE, # Search the entire subtree
        attributes=['cn', 'memberUid'] # Request common name (group name) and member UIDs
    )

    user_dict = dict() 
    for entry in conn.entries: 
        group_name = entry.cn.value # Extract the common name as the group name
        # Get member UIDs, handling cases where 'memberUid' attribute might be missing
        members = entry.memberUid.values if 'memberUid' in entry else [] 
        if members: 
            user_dict[group_name] = [m for m in members] 
            
    conn.unbind() # Close the LDAP connection
    return user_dict 

def get_ldap_users():
    """
    Connects to the LDAP server and retrieves a list of all user UIDs.
    Only retrieves entries with objectClass 'posixAccount'.
    """
    server = Server(LDAP_SERVER, get_info=ALL) 
    all_users = [] 

    conn = Connection(server, auto_bind=True) 
    conn.search(
        search_base=BASE_DN, 
        search_filter='(objectClass=posixAccount)', # Filter for posixAccount objects
        attributes=['uid', 'cn'] # Request user ID and common name
    )

    for entry in conn.entries: 
        if 'uid' in entry: 
            all_users.append(entry.uid.value) 
            
    conn.unbind() 
    return all_users 

def get_groups_by_user(groups: dict):
    """
    Transforms a dictionary of groups (group: [users]) into a dictionary
    of users (user: [groups]), indicating which groups each user belongs to.
    """
    user_group = {} 
    for group, users in groups.items(): 
        for user in users:
            user_group.setdefault(user, []).append(group) 
    return user_group 
 
def get_ldap_users_description(user):
    """
    Retrieves the description attribute for a specific LDAP user.
    """
    server = Server(LDAP_SERVER, get_info=ALL) 
    # conn = Connection(server, user=LDAP_USER, password=LDAP_PASSWORD, authentication=NTLM, auto_bind=True)
    

    conn = Connection(server, auto_bind=True) 
    conn.search(
        search_base=BASE_DN, 
        search_filter=f'(uid={user})', 
        search_scope=SUBTREE, 
        attributes=['cn', 'description'] 
    )
    description = ""
    
    for entry in conn.entries:
        description = f"{entry.description}"
    
    conn.unbind()

    return user, description 

# --- Slurm/System Utility Functions ---

def is_account_in_slurm(accounts: List[V0040Account], group: str) -> bool:
    """
    Checks if a given group (account) exists in the provided list of Slurm accounts.
    """
    
    if group in [account.name for account in accounts.accounts]:
        return True
    return False

def is_user_in_slurm(slurm_users: List[V0040User], user: str) -> bool:
    """
    Checks if a given user exists in the provided list of Slurm users.
    """
    
    if user in [slurm_user.name for slurm_user in slurm_users.users]:
        return True
    return False

def is_user_in_ldap(ldap_users: list, user: str, exceptions_list: list = []) -> bool:
    """
    Checks if a given user exists in the provided list of LDAP users,
    optionally including an exceptions list.
    """
    list_users = ldap_users + exceptions_list 
    if user in list_users: 
        return True
    return False

def is_account_in_ldap(ldap_groups: dict, group: str, exceptions_list: list = []) -> bool:
    """
    Checks if a given group (account) exists in the provided dictionary of LDAP groups,
    optionally including an exceptions list.
    """
    
    list_group = [ldap_group for ldap_group, ldap_users in ldap_groups.items()] + exceptions_list
    if group in list_group: 
        return True
    return False
    
def gen_token():
    """
    Generates a Slurm JWT token using the 'scontrol token' command.
    Returns the token string if successful, otherwise None.
    Handles potential errors like command not found or execution failures.
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
            print("Warning: 'SLURM_JWT=' not found in scontrol token output.") 

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


def add_user(user: str, account: str) -> V0040OpenapiResp:
    """
    Adds a user to SlurmDB with an initial association to a given account.
    """
    try:
        response = None
        v0040_openapi_users_resp = {
            "users":[{
                "name":user,
                "associations":[{
                    "account":account,
                    "cluster":CLUSTER, 
                    "user":user,
                }]                   
            }]
        }
        
        response = slurmdb.slurmdb_v0040_post_users(v0040_openapi_users_resp=v0040_openapi_users_resp)      
    except Exception as e:
        print(f"Error adding user {e}") 
    finally: 
        return response 

def del_user(user: str) -> V0040OpenapiResp:
    """
    Deletes a user from SlurmDB.
    """
    try:
        response = None
        
        response = slurmdb.slurmdb_v0040_delete_user(user)      
    except Exception as e:
        print(f"Error deleting user {e}")
    finally: 
        return response 

def add_account(group: str) -> V0040OpenapiResp:
    """
    Adds an account (group) to SlurmDB.
    """
    try:
        response = None
        
        v0040_openapi_accounts = {
            "accounts": [
                {
                "name": group,
                "description": f"Account for {group}",
                "organization": ORG, 
                }
            ]
        }
        
        response = slurmdb.slurmdb_v0040_post_accounts(v0040_openapi_accounts_resp=v0040_openapi_accounts)
    except Exception as e:
        print(f"Error adding ACCOUNT {e}") 
    finally: 
        return response 

def del_account(account: str) -> V0040OpenapiResp:
    """
    Deletes an account from SlurmDB.
    Note: There's a typo in the original code: `acount` should be `account`.
    """
    try:
        response = None
        response = slurmdb.slurmdb_v0040_delete_account(account) 
    except Exception as e:
        print(f"Error deleting account {e}") 
    finally: 
        return response 

def add_association(user: str, group: str) -> V0040OpenapiResp:
    """
    Adds an association between a user and a group (account) in SlurmDB.
    """
    try:
        response = None
        
        OpenapiUsersResp = {"associations":[{
            'account': group,
            'cluster': CLUSTER,
            'user': user,
            'parent_account': ORG,           
            }],
        }
        
        response = slurmdb.slurmdb_v0040_post_associations(v0040_openapi_assocs_resp=OpenapiUsersResp)
    except Exception as e:
        print(f"Error adding association {e}") 
    finally: 
        return response 

# --- Main Execution Block ---

if __name__ == "__main__":
    
    c = Config() # Create a configuration object
    c.host = BASE_URL # Set the base URL for the Slurm API (assumed to be a global constant)
    #slurm = SlurmApi(Client(c)) # Initialize Slurm API client
    slurmdb = SlurmdbApi(Client(c)) # Initialize SlurmDB API client
    
    # Retrieve LDAP data
    dict_groups = get_ldap_users_by_group() 
    dict_users = get_groups_by_user(dict_groups) # Transform to user-to-groups mapping
    list_ldap_users = get_ldap_users() #
    
    # Generate Slurm API token
    c.access_token = gen_token() 
    
    # Retrieve current Slurm data
    slurm_users = slurmdb.slurmdb_v0040_get_users() # Get all users from SlurmDB
    slurm_list_users = [slurm_user.name for slurm_user in slurm_users.users] # Extract user names
    slurm_accounts = slurmdb.slurmdb_v0040_get_accounts() # Get all accounts from SlurmDB
    
    # Synchronize users from LDAP to Slurm
    for user, list_of_accounts in dict_users.items(): 
        if not (is_user_in_slurm(slurm_users, user)): 
            for account in list_of_accounts:
                response = add_user(user, account) # Add the user to Slurm with an association to that account

    # Synchronize users from Slurm to LDAP (delete users in Slurm not found in LDAP)
    # 'exceptions_list'  predefined global list for users that should not be deleted
    for slurm_user in slurm_list_users:  
        if not is_user_in_ldap(list_ldap_users, slurm_user, exceptions_list):
            del_user(slurm_user) # Delete the user from Slurm
            print(f"User {slurm_user} deleted")

    # Synchronize groups/accounts and associations
    # 'exceptions_list'  predefined global list for groups that should not be deleted
    for group, users_list in dict_groups.items():      
        if not is_account_in_ldap(dict_groups, group, exceptions_list):
            del_account(group) 
            print(f"Account {group} deleted")
        for user in users_list: 
            response_account = add_account(group) # Ensure the account exists in Slurm
            response_assoc = add_association(user, group) # Add/update the association between user and group

