# sacct-ldap-sync
## LDAP and Slurm Synchronization Script
This Python script facilitates the synchronization of user and group (account) information between an LDAP directory and a Slurm workload manager's database (SlurmDB). It leverages ldap3 for LDAP interactions and a generated Slurm REST API client for SlurmDB operations.

# Features
* LDAP User and Group Retrieval: Fetches users and their group memberships from an LDAP server.
* Slurm Integration: Interacts with SlurmDB to manage users, accounts, and their associations.
* User Synchronization: Adds LDAP users to SlurmDB if they don't exist.
* User Admin: add admin users
* Extra associations: With config file is posible to add new associations
* User De-provisioning: Deletes users from SlurmDB if they no longer exist in LDAP (with configurable exceptions).
* Account Synchronization: Adds accounts (groups) to SlurmDB based on LDAP groups.
* Association Management: Creates or updates user-account associations in SlurmDB.
* Slurm Token Generation: Automatically generates a Slurm JWT token for API authentication.

# Execution

main.py  <config_file>

# NOTES 

* Slurm REST API Client: The script assumes you have a generated Python client for the Slurm REST API. This client typically comes from an OpenAPI/Swagger specification of the Slurm REST API. You'll need to generate this client and ensure it's accessible in your Python environment.

# Config File Variables/Configuration:
Config file is a yaml format config file with next parameters 

* * DefaultOrganization: Organization for slurm (str)
* * DefaultAccount: Default account in this version is assigned the same to all users (str)
* * Cluster: Slurm cluster Name (str)
* * NoLDAPUsersList: Users that are not in ldap and must be created in slurm accounts (List(str))
* * NoLDAPAccountsList: Accounts not in ldap that must be created and not deleted (List(str))
* * NoSlurmUsersList: Users that are in ldap but not belong to SLURM (List(str))
* * NoSlurmAccountsList: Ldap Groups that we don't want to create on Slurm accounting (List(str))
* * ExtraLDAPUserAssociations: Extra associations that is going to be created in Slurm accounting (Dic(user:(str),Accounts:list(str)))
* * AdminUsersList: Users that going to have users rigtht on slurm (List(str))
* * SlurmAPIURL: Url and port where slurmrest is pulishing the API "http://localhost:6832" (str)
* * SlurmJWTToken: Slurm token create with scontrol token lifespan=INFINITE (str)
* * LdapServer : Ldap server url 'ldap://localhost' 
* * LdapBaseDN : ldap base DN 'DC=mydomain,DC=local'
* * LoggingLevel: login level only accepted "INFO", "DEBUG","ERROR"

# TODO

* Add Coordinator and Operator Admin levels
* Create QOS
* Add parameters in associations like limits
* Select default acount by user
* Delete Accounts
* Delete associations
* Delete QOS
