from ldap3 import Server, Connection, ALL, SUBTREE

class ldaplib:
    
    def __init__(self,LdapServer='ldap://localhost',BaseDN='DC=nextmol,DC=local',):
        self.LDAP_SERVER = LdapServer
        self.BASE_DN = BaseDN
        server = Server(self.LDAP_SERVER, get_info=ALL)
        self.conn = Connection(server,auto_bind=True)

    def get_groups_list(self):
        self.conn.search(
            search_base=self.BASE_DN,
            search_filter='(objectClass=posixGroup)',  
            search_scope=SUBTREE,
            attributes=['cn', 'gidNumber']  
        )
        return [(group.cn.value,group.gidNumber.value) for group in self.conn.entries]
        
    def get_users_list(self):
        
        self.conn.search(
            search_base=self.BASE_DN,
            search_filter='(objectClass=posixAccount)',  
            search_scope=SUBTREE,
            attributes=['uid', 'uidNumber','gidNumber']  
        )
        return [(user.uid.value,user.uidNumber.value,user.gidNumber.value) for user in self.conn.entries]
      
    def get_secondary_group_list(self):
        self.conn.search(
            search_base=self.BASE_DN,
            search_filter='(objectClass=posixGroup)',  
            search_scope=SUBTREE,
            attributes=['cn','gidNumber','memberUid']  
        )
        return {group.cn.value : group.memberUid.value for group in self.conn.entries if group.memberUid.value is not None}
    
    def get_user_groups(self, username):
        self.conn.search(
            search_base=self.BASE_DN,
            search_filter=f'(&(objectClass=posixGroup)(memberUid={username}))',  
            search_scope=SUBTREE,
            attributes=['cn', 'gidNumber']  
        )
        return [(group.cn.value,group.gidNumber.value) for group in self.conn.entries]
    
    def get_group_name_from_gid(self, gid):
        try:
            self.conn.search(
                search_base=self.BASE_DN,
                search_filter=f'(&(objectClass=posixGroup)(gidNumber={gid}))',  
                search_scope=SUBTREE,
                attributes=['cn']  
            )
            if not self.conn.entries:
                return None
            return self.conn.entries[0].cn.value
        except Exception:
            return None            
        
    def get_user_info(self, username):
        try:
            self.conn.search(
                search_base=self.BASE_DN,
                search_filter=f'(&(objectClass=posixAccount)(cn={username}))',  
                search_scope=SUBTREE,
                attributes=['uid', 'uidNumber','gidNumber']  
            )    
            if not self.conn.entries:
                return None
            user = self.conn.entries[0]
            attrs = ['uid', 'uidNumber', 'gidNumber']
            converters = [str, int, int] 
            values = map(lambda pair: pair[1](getattr(user, pair[0]).value), zip(attrs, converters))
            return tuple(values)
        except Exception:
            return None            
      
    def get_all_groups_from_user(self, username):   
        try:
            userinfo=self.get_user_info(username)
            if userinfo is None:
                return None 
            usergroups=self.get_user_groups(username)
            return usergroups + [(self.get_group_name_from_gid(userinfo[2]), userinfo[2])]
        except Exception as e:
            print(f"An error occurred while retrieving groups for user {username}: {e}")
            return None
    
    def get_tuple_user_info(self, username):
        try:
            grouplist=self.get_all_groups_from_user(username)
            if grouplist is None:
                return None 
            return [(username,group)for group in grouplist]
        except Exception as e:  
            print(f"An error occurred while retrieving tuple user info for user {username}: {e}")
            return None
                       
        
    def __del__(self):
        self.conn.unbind()


    