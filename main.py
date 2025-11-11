from asyncio import subprocess
import ldaplib
import SlurmAccountManagerV41



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
    
    
def create_slurm_accounts_from_ldap(ldap,slurm,excetionlist=["root"],organization="nextmol"):
    ldap = ldaplib.ldaplib()
    groups = ldap.get_groups_list()
    for group in groups:
        if group not in excetionlist:
            account_name=group[0]
            if not account_name:
                print(f"  - No groups found for group {account_name}, skipping Slurm account creation.")
            else:
                slurm_account=slurm.post_account(account_name, organization)
                print(f"Slurm account creation response: {slurm_account.errors}")


def create_slurm_association(ldap,slurm,excetionlist=["root","easybuild"],organization="nextmol"):
    ldap = ldaplib.ldaplib()
    users = ldap.get_users_list()
    user_list = list(map(lambda x: x[0], users))
    clean_userlist=list(set(user_list)-set(excetionlist))   
    for username in clean_userlist:
        groups=[group for group,gid in ldap.get_all_groups_from_user(username)]
        print(f"User {username} has groups: {groups}")

        create_association=slurm.post_association(username,groups)
        print(f"Slurm association creation response: {create_association}")
        slurm_account=slurm.post_user(username,groups)
        print(f"Slurm user creation response: {slurm_account}")
        create_account_association=slurm.post_account_association(username,groups)
        print(f"Slurm account association creation response: {create_account_association}")
        create_user_association=slurm.post_user_association(username,groups)
        print(f"Slurm user association creation response: {create_user_association}")
    print(slurm.get_associations_list(self):
)



    

def main():
    exceptions=["easybuild","root"]
    slurm=SlurmAccountManagerV41.SlurmAccountManagerV41(jwt_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjM2OTUyNzcsImlhdCI6MTc2MjY5NTI3Nywic3VuIjoicm9vdCJ9.WAhHs3cN2QZ_-NvDmvKPbiPpxh6iPv8iDlBuklktatY")
    ldap = ldaplib.ldaplib()
    create_slurm_accounts_from_ldap(ldap,slurm)
    create_slurm_association(ldap,slurm,exceptions)
    






if __name__ == "__main__":

    main()