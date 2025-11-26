from openapi_client import Configuration
from openapi_client.api.slurmdb_api import SlurmdbApi
from openapi_client.api.slurm_api import SlurmApi
from openapi_client import ApiClient as Client 
from openapi_client import ApiException
from enum import Enum
from typing import Optional, List


class AdminLevel(Enum):
    ADMIN = "Administrator"
    OPERATOR = "Operator"
    NONE = "None"

class AssociationExistsError(Exception):
    def __init__(self, message, username, accountnames):
        self.username = username
        self.accountnames = accountnames
        message = (
            f"{message}: User '{self.username}' is already associated with accounts "
            f"{', '.join(self.accountnames)}"
        )
        super().__init__(message)
        
class SlurmAccountManagerV41:
    def __init__(self, api_url="http://10.0.0.13:6820", jwt_token=""):
        slurm_config = Configuration()
        slurm_config.host = api_url
        slurm_config.access_token = jwt_token
        self.slurm_api = SlurmApi(Client(slurm_config))
        self.slurmdb_api = SlurmdbApi(Client(slurm_config))
    
    def get_accounts_list(self):
        try:
            accounts = self.slurmdb_api.slurmdb_v0041_get_accounts()
            return [(account.name,account.organization) for account in accounts.accounts]
        except Exception as e:
            print(f"An error occurred while listing accounts: {e}")

    def get_associations_list(self):
        try:
            associations = self.slurmdb_api.slurmdb_v0041_get_associations()
            return [(assoc.user, assoc.account) for assoc in associations.associations
                     if assoc.user and assoc.user.strip() != '']
        except Exception as e:
            print(f"An error occurred while listing associations: {e}")
    
    def get_users_list(self):
        try:
            users = self.slurmdb_api.slurmdb_v0041_get_users()
            return [(user.name, user.associations) for user in users.users]
        except Exception as e:
            print(f"An error occurred while listing users: {e}")
    
    def post_user(self, username:str, admin_level: Optional[AdminLevel] = None):
        try:
          
            v0041_openapi_slurmdbd_config_resp_users_inner = [
                {
                 "name": username,
                 "administrator_level": [admin_level],
                }]
            response = self.slurmdb_api.slurmdb_v0041_post_users( {
                "users": v0041_openapi_slurmdbd_config_resp_users_inner,
                })
            return response
        except ApiException as e:  
            if e.status == 304:
                raise AssociationExistsError("User already exist.",username, []) from e  
            else:
                print(f"An unexpected API error occurred during user creation: {e}")
                return None
        except Exception as e:
            print(f"An error occurred while creating user {username}: {e}")
    
    def post_account(self, account_name, organization):
        try:
            account_body = {
                "name": account_name,
                "organization": organization,
                "description": "Created via LDAP sync script"
            }
            response = self.slurmdb_api.slurmdb_v0041_post_accounts({"accounts":[account_body]})
            return response
        except ApiException as e:  
            if e.status == 304:
                raise AssociationExistsError("Account already exist.",account_name, organization) from e  
            else:
                print(f"An unexpected API error occurred during account creation: {e}")
                return None
        except Exception as e:
            print(f"An error occurred while creating account {account_name}: {e}")
            return None

    def post_association(self, username:str, accounts:list, cluster="nanoscope"):
        try:
            v0041_assoc_default={
                "qos":"normal"
            }
            v0041_assoc=[{
                "account":account_name,
                "cluster":cluster,
                "default":v0041_assoc_default,
                "user":username
            }
            for account_name in accounts]
            v0041_openapi_assocs_resp = {
                "associations":v0041_assoc
            }
            response = self.slurmdb_api.slurmdb_v0041_post_associations(v0041_openapi_assocs_resp)
            return response
        except ApiException as e: 
            if e.status == 304:
                raise AssociationExistsError("Association already exist.",username, accounts) from e           
            else:
                print(f"An unexpected API error occurred during association creation: {e}") 
        except Exception as e:
            print(f"An error occurred while creating association of user {username} with account {accounts}: {e}")      
    

    def post_account_association(self, username:str, accountnames:list,organization="nextmol"):
        try:
            slurmdb_v0041_post_users_association_request_association_condition_association={
                "comment": "Created via LDAP sync script",
                "defaultqos":"normal"
            }
            slurmdb_v0041_post_accounts_association_request_account={
                "Description": "Created via LDAP sync script",
                "organization": organization
            }
            slurmdb_v0041_post_accounts_association_request_association_condition={
                "accounts": accountnames,
                "association":slurmdb_v0041_post_users_association_request_association_condition_association
            }
            slurmdb_v0041_post_accounts_association_request={
                "association_condition": slurmdb_v0041_post_accounts_association_request_association_condition,
                "account":slurmdb_v0041_post_accounts_association_request_account
            }
            response=self.slurmdb_api.slurmdb_v0041_post_accounts_association(
                slurmdb_v0041_post_accounts_association_request=slurmdb_v0041_post_accounts_association_request)
            return response
        
        except ApiException as e: 
            if e.status == 304:
                print(e)
                raise AssociationExistsError("Association already exist.",username, accountnames) from e           
            else:
                print(f"An unexpected API error occurred during association creation: {e}")
                return None
        except Exception as e:
            print(f"An unexpected error occurred during API communication: {e}")
            return None
    
    def post_user_association(self, username, accountnames, cluster="nanoscope", defaultaccount="nextmol"):
        try:
            slurmdb_v0041_post_users_association_request_association_condition_association={
                "comment": "Created via LDAP sync script",
                "defaultqos":"normal"
            }
            slurmdb_v0041_post_users_association_request_association_condition={
                "accounts": accountnames,
                "clusters": [cluster],
                "association":slurmdb_v0041_post_users_association_request_association_condition_association,
                "users":[username]
            }
            slurmdb_v0041_post_users_association_request_user={
                "defaultaccount": defaultaccount
            }

            slurmdb_v0041_post_users_association_request={
                "association_condition": slurmdb_v0041_post_users_association_request_association_condition,
                "user": slurmdb_v0041_post_users_association_request_user
            }
            response=self.slurmdb_api.slurmdb_v0041_post_users_association(slurmdb_v0041_post_users_association_request=slurmdb_v0041_post_users_association_request)
            return response
        except ApiException as e: 
            if e.status == 304:
                print(e)
                raise AssociationExistsError("Association already exist.",username, accountnames) from e           
            else:
                print(f"An unexpected API error occurred during association creation: {e}")
                return None
        except Exception as e:
            print(f"An unexpected error occurred during API communication: {e}")
            return None
        
        
    def delete_user(self, username):
        try:
            response = self.slurmdb_api.slurmdb_v0041_delete_user(username)
            return response
        except Exception as e:
            print(f"An error occurred while deleting user {username}: {e}")

    def delete_account(self, account_name): 
        try:
            response = self.slurmdb_api.slurmdb_v0041_delete_account(account=account_name)
            return response
        except Exception as e:
            print(f"An error occurred while deleting account {account_name}: {e}")
    
    def delete_association(self, username, account_name):
        try:
            response = self.slurmdb_api.slurmdb_v0041_delete_association(user=username, account=account_name)
            return response
        except Exception as e:
            print(f"An error occurred while deleting association of user {username} with account {account_name}: {e}")
    
