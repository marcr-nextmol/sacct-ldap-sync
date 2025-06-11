# sacct-ldap-sync
## LDAP and Slurm Synchronization Script
This Python script facilitates the synchronization of user and group (account) information between an LDAP directory and a Slurm workload manager's database (SlurmDB). It leverages ldap3 for LDAP interactions and a generated Slurm REST API client for SlurmDB operations.

# Features
* LDAP User and Group Retrieval: Fetches users and their group memberships from an LDAP server.
* Slurm Integration: Interacts with SlurmDB to manage users, accounts, and their associations.
* User Synchronization: Adds LDAP users to SlurmDB if they don't exist.
* User De-provisioning: Deletes users from SlurmDB if they no longer exist in LDAP (with configurable exceptions).
* Account Synchronization: Adds accounts (groups) to SlurmDB based on LDAP groups.
* Association Management: Creates or updates user-account associations in SlurmDB.
* Slurm Token Generation: Automatically generates a Slurm JWT token for API authentication.

# Prerequisites
Before running this script, ensure you have the following:

* Python 3.x: The script is written in Python.
* ldap3 library: Install using pip:
```Bash
pip install ldap3
```
* openapi installation using pip
```Bash
pip install .py_api_client
```
* Slurm REST API Client: The script assumes you have a generated Python client for the Slurm REST API. This client typically comes from an OpenAPI/Swagger specification of the Slurm REST API. You'll need to generate this client and ensure it's accessible in your Python environment.
* Slurm Installation: A running Slurm cluster with scontrol command accessible in the PATH for token generation.
* Environment Variables/Configuration:
* * LDAP_SERVER: The hostname or IP address of your LDAP server.
* * BASE_DN: The base distinguished name for your LDAP searches (e.g., "dc=example,dc=com").
* * CLUSTER: The name of your Slurm cluster.
* * ORG: The organization name for Slurm accounts.
* * BASE_URL: The base URL for the Slurm REST API (e.g., "http://localhost:6820/slurm/v0.0.40").
* * exceptions_list: []