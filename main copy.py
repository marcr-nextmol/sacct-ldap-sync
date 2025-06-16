from ldap3 import Server, Connection, ALL, NTLM, SUBTREE
import requests
import json
import os
import sys
from openapi_client.models.new_slurm_account import NewSlurmAccount
from openapi_client.models.new_slurm_user import NewSlurmUser
from openapi_client.models.slurm_account import SlurmAccount
from openapi_client.models.slurm_user import SlurmUser
from openapi_client import ApiClient as client
from openapi_client import Configuration as Config
from openapi_client.apis.tags.slurm_api import SlurmApi 
from openapi_client.apis.tags.slurmdb_api import SlurmdbApi

# Configuration
LDAP_SERVER = 'ldap://localhost'
BASE_DN = 'DC=nextmol,DC=local'
BASE_URL = "http://10.0.0.2:6820/slurmdb/v0.0.41"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjM4OTY3MTMwMDUsImlhdCI6MTc0OTIyOTM1OSwic3VuIjoicm9vdCJ9.ypZj8mDYOEvXYbiaJC9xTi6NqTJWfINdp6N-ABHUoag"

c.host="http://10.0.0.2:6820"
slurm=SlurmApi(Cleint(c))
slurmdb=SlurmdbApi(Cleint(c))

def get_ldap_users_by_group():
    server = Server(LDAP_SERVER, get_info=ALL)
    #conn = Connection(server, user=LDAP_USER, password=LDAP_PASSWORD, authentication=NTLM, auto_bind=True)

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
        print(members)
        if members:
            user_dict[group_name] = [m for m in members]
            
    conn.unbind()
    return user_dict 

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
        search_filter=f'(uid={user})',  # or '(sAMAccountName=jdoe)' for AD
        search_scope=SUBTREE,
        attributes=['cn', 'description']
    )
    description=""
    
    for entry in conn.entries:       
        description = f"{entry.description}"
    
    conn.unbind()

    return user,description



def make_request(method, endpoint, data=None, params=None):
    """
    Makes an HTTP request to the Slurm API.

    Args:
        method (str): HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE').
        endpoint (str): The API endpoint relative to the BASE_URL.
        data (dict, optional): JSON payload for POST/PUT requests. Defaults to None.
        params (dict, optional): Query parameters for GET requests. Defaults to None.

    Returns:
        tuple: A tuple containing (response_json_or_text, status_code).
    """
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-SLURM-USER-TOKEN": API_KEY  # Include the API key in the header
    }

    print(f"\n--- Making {method} \n request to {url} ---")
    print(f"Request Data: {json.dumps(data, indent=2) if data else 'None'}")

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, json=data) # DELETE with body if removing member
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        print(f"Response Status Code: {response.status_code}")
        try:
            response_content = response.json()
            print(f"Response Body: {json.dumps(response_content, indent=2)}")
        except json.JSONDecodeError:
            response_content = response.text
            print(f"Response Body (text): {response_content}")

        return response_content, response.status_code
    except requests.exceptions.ConnectionError:
        print(f"ERROR: Could not connect to the API server at {BASE_URL}.")
        print("Please ensure the API server is running.")
        return {"error": "Connection failed"}, None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return {"error": str(e)}, None

def add_user(username: str,accounts: list):
    """Adds a new Slurm user."""
    assoc=list()
    for account in accounts:
        assoc.append({"name":username,"account":account})
    user_data = {"users":[{
        "name": username,
        "association":assoc
        }]
    }
    return make_request("POST", "/users", data=user_data)

def get_user(username):
    """Gets details of a specific Slurm user."""
    return make_request("GET", f"/users/{username}")

def modify_user(username, **kwargs):
    """Modifies an existing Slurm user."""
    accounts=kwargs.get('accounts',[])
    cluster=kwargs.get('cluster',[])
    assoc={"associations":[]}
    for account in accounts:
        assoc["associations"].append({"name":username,"account":account,"cluster":cluster})
    user_data = {k: v for k, v in kwargs.items() if v is not None}
    return make_request("PUT", f"/users/{username}", data=assoc)

def remove_user(username):
    """Removes a Slurm user."""
    return make_request("DELETE", f"/users/{username}")

def create_account(account_name, description, organization="nextmol", coordinator=None):
    """Creates a new Slurm account."""
    
    account={"accounts":[{
        "name": account_name,
        "description": description,
        "organization": organization,
        }]
    }
    
    print(type(account))
    return make_request("POST", "/accounts", data=account)


def modify_accounts(username, **kwargs):
    """Modifies an existing Slurm user."""
    accounts=kwargs.get('accounts',[])
    cluster=kwargs.get('cluster',[])
    assoc={"associations":[]}
    for account in accounts:
        assoc["associations"].append({"user":username,"account":account,"cluster":cluster})
    return make_request("PUT", f"/accounts_association", data=assoc)

def get_account(account_name):
    """Gets details of a specific Slurm account."""
    return make_request("GET", f"/accounts/{account_name}")

def remove_account(account_name):
    """Removes a Slurm account."""
    return make_request("DELETE", f"/accounts/{account_name}")

def add_member_to_account(account_name, username):
    """Adds a member to a Slurm account."""
    member_data = {"username": username}
    return make_request("POST", f"/accounts/{account_name}/members", data=member_data)

def remove_member_from_account(account_name, username):
    """Removes a member from a Slurm account."""
    member_data = {"username": username}
    return make_request("DELETE", f"/accounts/{account_name}/members", data=member_data)

def list_accounts():
    """Lists all Slurm accounts."""
    slurm_accounts=make_request("GET", "/accounts")[0].get("accounts",[])
    print(slurm_accounts)
    return [accaunt_dict.get("name") for accaunt_dict in slurm_accounts]
    

def list_users():
    """Lists all Slurm users."""
    slurm_users=make_request("GET", "/users")[0].get("users",[])
    return [user_dict.get("name") for user_dict in slurm_users]



# --- Demonstration of API Calls ---
if __name__ == "__main__":
    dict_groups=get_ldap_users_by_group()
    dict_groups['nextmol']=["mrodriguez"]
    dict_users=get_groups_by_user(dict_groups)
    slurm_users=list_users()
    slurm_accounts=list_accounts()
    for user, list_of_accounts in dict_users.items():
        for account in list_of_accounts:  
            if account not in slurm_accounts:
                print("Create Accout")
                response, status = create_account(account,"Group Description")
                if status == 201:
                    print(f"Account {account} created successfully.")
                elif status == 409:
                    print(f"Account {account} already exists.")
        if user not in slurm_users:
            print(f"{user} not exist")
            add_user(user,list_of_accounts)
        else:
            print(f"{user} modified")
            modify_accounts(user,accounts=list_of_accounts,cluster="nanoscope")

        