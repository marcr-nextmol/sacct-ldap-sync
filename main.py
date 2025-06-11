import openapi_client
import subprocess
from ldap3 import Server, Connection, ALL, NTLM, SUBTREE
from openapi_client import ApiClient as Client 
from openapi_client import Configuration as Config
from openapi_client.api.slurm_api import SlurmApi 
from openapi_client.api.slurmdb_api import SlurmdbApi 
from openapi_client.models.v0040_account import V0040Account
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.models.v0040_user import V0040User
from typing import List, Optional



######## Configuration####################

LDAP_SERVER = 'ldap://localhost'
BASE_DN = 'DC=nextmol,DC=local'
BASE_URL = "http://10.0.0.2:6820"
CLUSTER = "nanoscope"
ORG = "nextmol"
exceptions_list = [ "easybuild","root" ]

############################################

def get_ldap_users_by_group():
    server = Server(LDAP_SERVER, get_info=ALL)

    conn = Connection(server,auto_bind=True)
    conn.search(
        search_base=BASE_DN,
        search_filter='(objectClass=posixGroup)',  
        search_scope=SUBTREE,
        attributes=['cn', 'memberUid']  
    )

    user_dict=dict()
    for entry in conn.entries:
        group_name = entry.cn.value
        members = entry.memberUid.values if 'memberUid' in entry else []
        if members:
            user_dict[group_name] = [m for m in members]
            
    conn.unbind()
    return user_dict 

def get_ldap_users():
    server = Server(LDAP_SERVER, get_info=ALL)
    all_users = []

    conn = Connection(server,auto_bind=True)
    conn.search(
        search_base=BASE_DN,
        search_filter='(objectClass=posixAccount)',  
        attributes=['uid', 'cn'] 
    )

    for entry in conn.entries:
        if 'uid' in entry:
            all_users.append(entry.uid.value)
            
    conn.unbind()
    return all_users


def get_groups_by_user(groups: dict ):
    user_group = {}
    for group, users in groups.items():
        for user in users:
            user_group.setdefault(user, []).append(group)
    return user_group
 
def get_ldap_users_description(user):
    server = Server(LDAP_SERVER, get_info=ALL)
    #conn = Connection(server, user=LDAP_USER, password=LDAP_PASSWORD, authentication=NTLM, auto_bind=True)

    conn = Connection(server,auto_bind=True)
    conn.search(
        search_base=BASE_DN,
        search_filter=f'(uid={user})', 
        search_scope=SUBTREE,
        attributes=['cn', 'description']
    )
    description=""
    
    for entry in conn.entries:       
        description = f"{entry.description}"
    
    conn.unbind()

    return user,description


def is_account_in_slurm(accounts: List[V0040Account],group: str ) -> bool :
    if group in [account.name for account in accounts.accounts ]:
        return True
    return False

def is_user_in_slurm(slurm_users: List[V0040User],user: str ) -> bool :
    if user in [slurm_user.name for slurm_user in slurm_users.users ]:
        return True
    return False


def is_user_in_ldap(ldap_users: list ,user: str, exceptions_list: list = []) -> bool :
    list_users = ldap_users + exceptions_list
    if user in list_users:
        return True
    return False

def is_account_in_ldap(ldap_groups: dict ,group: str, exceptions_list: list = []) -> bool :
    list_group = [ ldap_group for  ldap_group, ldap_users in ldap_groups.items()] + exceptions_list
    if group in list_group:
        return True
    return False
    
    
def gen_token():
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
    try:
        response=None
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
        response=slurmdb.slurmdb_v0040_post_users(v0040_openapi_users_resp=v0040_openapi_users_resp)      
    except Exception as e:
        print(f"Error adding user {e}")
    finally: 
        return response

def del_user(user: str) -> V0040OpenapiResp:
    try:
        response=None
        response=slurmdb.slurmdb_v0040_delete_user(user)      
    except Exception as e:
        print(f"Error adding user {e}")
    finally: 
        return response

def add_account(group: str) -> V0040OpenapiResp:
    try:
        response=None
        v0040_openapi_accounts = {
            "accounts": [
                {
                "name": group,
                "description": f"Account for {group}",
                "organization": ORG,
                }
            ]
        }
        response=slurmdb.slurmdb_v0040_post_accounts(v0040_openapi_accounts_resp=v0040_openapi_accounts)
    except Exception as e:
        print(f"Error adding ACCOUNT {e}")
    finally: 
        return response

def del_account(account: str) -> V0040OpenapiResp:
    try:
        response=None
        response=slurmdb.slurmdb_v0040_delete_account(acount)      
    except Exception as e:
        print(f"Error adding user {e}")
    finally: 
        return response


def add_association(user: str, group: str) -> V0040OpenapiResp:
    try:
        response=None
        OpenapiUsersResp= {"associations":[{'account': group,
            'cluster': CLUSTER,
            'user': user,
            'parent_account':ORG,           
            }],
        }
        response=slurmdb.slurmdb_v0040_post_associations(v0040_openapi_assocs_resp=OpenapiUsersResp)
    except Exception as e:
        print(f"Error adding ACCOUNT {e}")
    finally: 
        return response


if __name__ == "__main__":
    c = Config()
    c.host = BASE_URL
    slurm = SlurmApi(Client(c))
    slurmdb = SlurmdbApi(Client(c))
    
    dict_groups = get_ldap_users_by_group()
    dict_users = get_groups_by_user(dict_groups)
    list_ldap_users = get_ldap_users()
    
    c.access_token = gen_token()
    
    slurm_users = slurmdb.slurmdb_v0040_get_users()
    slurm_list_users = [slurm_user.name for slurm_user in slurm_users.users ]
    slurm_accounts = slurmdb.slurmdb_v0040_get_accounts()
    
    for user, list_of_accounts in dict_users.items():
        if not (is_user_in_slurm(slurm_users,user)):
            for account in list_of_accounts:
                response=add_user(user,account)

    for slurm_user in slurm_list_users:  
        if not is_user_in_ldap(list_ldap_users, slurm_user, exceptions_list):
            del_user(slurm_user)
            print(f"User {slurm_user} deleted" )


    for group, users_list in dict_groups.items():      
        if not is_account_in_ldap(dict_groups, group, exceptions_list):
            del_user(group)
            print(f"Account {group} deleted" )

        for user in users_list:
            response_account = add_account(group)
            response_assoc = add_association(user,group)





