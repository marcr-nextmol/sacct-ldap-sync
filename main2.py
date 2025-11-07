import requests
import json
import os
from pprint import pprint
from ldap3 import Server, Connection, ALL, SUBTREE, LEVEL, ALL_ATTRIBUTES
from collections import defaultdict

# --- Configuration ---
# You need to configure these based on your Slurm REST API setup
SLURM_API_URL = "http://10.0.0.2:6820"
API_VERSION = "v0.0.41"  # Check your slurmrestd version
SLURM_JWT="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjE1NjM1ODMsImlhdCI6MTc2MTU2MTc4Mywic3VuIjoicm9vdCJ9.h64zy_bLvidCYFnQoSzDJwIoJCvsy4-r0mWs-lmwoQQ"

LDAP_SERVER = 'ldap://localhost'
BASE_DN = 'DC=nextmol,DC=local'
CLUSTER = "nanoscope"
ORG = "nextmol"
exceptions_list = [ "easybuild","root" ]

# --- API Endpoint ---
# The endpoint to get all registered users from the Slurm Database
USERS_ENDPOINT = f"/slurmdb/{API_VERSION}/users"
ACCOUNTS_ENDPOINT = f"/slurmdb/{API_VERSION}/accounts"


# --- Authentication Headers ---
HEADERS = {
    'X-SLURM-USER-TOKEN': SLURM_JWT,
    'Accept': 'application/json'
}

def get_slurm_users():
    """Fetches and prints registered Slurm users via the REST API."""
    if not SLURM_JWT:
        print("Error: SLURM_JWT environment variable not set.")
        print("Run 'export $(scontrol token)' to get a valid token.")
        return

    print(f"Attempting to connect to: {SLURM_API_URL + USERS_ENDPOINT}")

    try:
        response = requests.get(
            SLURM_API_URL + USERS_ENDPOINT,
            headers=HEADERS,
            verify=False # Set to True if using HTTPS with a trusted certificate
        )
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        data = response.json()
        
        # The user list is typically nested under a 'users' key in the response
        user_list = data.get('users', [])
        
        print(f"\nSuccessfully retrieved {len(user_list)} registered user(s).")
        print("-" * 40)
        for user in user_list:
            name = user.get('name')
            account = user.get('default')
            print(f"User: {name}  Default Account: {account['account']:<15}")

    except requests.exceptions.HTTPError as errh:
        print(f"\nHTTP Error: {errh}")
        print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError as errc:
        print(f"\nConnection Error: {errc}")
        print("Check if slurmrestd is running and the URL is correct.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def get_slurm_accounts():
    """Fetches and prints registered Slurm users via the REST API."""
    if not SLURM_JWT:
        print("Error: SLURM_JWT environment variable not set.")
        print("Run 'export $(scontrol token)' to get a valid token.")
        return

    print(f"Attempting to connect to: {ACCOUNTS_ENDPOINT}")

    try:
        response = requests.get(
            SLURM_API_URL + ACCOUNTS_ENDPOINT,
            headers=HEADERS,
            verify=False 
        )
        
        response.raise_for_status()

        data = response.json()
        accounts_list = data.get('accounts', [])

        print(f"\nSuccessfully retrieved {len(accounts_list)} registered user(s).")
        print("-" * 40)
        for account in accounts_list:
            name = account.get('name')
            print(f"Accont: {name}  ")

    except requests.exceptions.HTTPError as errh:
        print(f"\nHTTP Error: {errh}")
        print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError as errc:
        print(f"\nConnection Error: {errc}")
        print("Check if slurmrestd is running and the URL is correct.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def get_openldap_users_and_groups():
    """
    Retrieves OpenLDAP users and their primary groups, organizing them
    as a dictionary where keys are group names and values are lists of users.
    
    Returns:
        dict: A dictionary of {group_name: [user1, user2, ...]}
              or an empty dictionary if an error occurs or no data is found.
    """
    
    server = Server(LDAP_SERVER, get_info=ALL)
    result_dict = {}
    try:
        with Connection(server, auto_bind=True) as conn:
            
       
            group_search_result = conn.search(
                search_base=BASE_DN,
                search_filter='(objectClass=posixGroup)',  
                search_scope=SUBTREE,
                attributes=['cn', 'gidNumber']
            )

            if not group_search_result:
                print("Error: Group search failed or returned no data.")
                return {}
            group_dict = {}
            for entry in conn.entries:
                cn_val = entry['cn'].value
                gid_val = entry['gidNumber'].value
                
                if cn_val and gid_val is not None:
                    try:
                        group_dict[int(gid_val)] = cn_val
                    except ValueError:
                        print(f"Warning: Could not convert gidNumber '{gid_val}' to integer for group '{cn_val}'. Skipping.")
            user_search_result = conn.search(
                search_base=BASE_DN,
                search_filter='(objectClass=posixAccount)',
                search_scope=SUBTREE,
                attributes=['uid', 'gidNumber']
            )

            if not user_search_result:
                print("Error: User search failed or returned no data.")
                return {}
            user_dict = {}
            for entry in conn.entries:
                uid_val = entry['uid'].value
                gid_val = entry['gidNumber'].value

                if uid_val and gid_val is not None:
                    try:
                        user_dict[uid_val] = int(gid_val)
                    except ValueError:
                        print(f"Warning: Could not convert gidNumber '{gid_val}' to integer for user '{uid_val}'. Skipping.")
            result_dict = defaultdict(list)
            for user, gid in user_dict.items():
                group_name = group_dict.get(gid)
                if group_name:
                    result_dict[group_name].append(user)
                    
        return dict(result_dict)

    except Exception as e:
        print(f"An error occurred during LDAP operation: {e}")
        return {}
    

if __name__ == "__main__":
    get_slurm_users()
    get_slurm_accounts()
