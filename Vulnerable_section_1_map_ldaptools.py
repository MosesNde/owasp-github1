             return self.get_name_bare(uun, l)
 
     def get_name_bare(self, uun, l):
        ldap_filter = "uid=" + uun
         data = l.search_s(self.config['memberdn'], ldap.SCOPE_SUBTREE, ldap_filter, None)
 
         if data: