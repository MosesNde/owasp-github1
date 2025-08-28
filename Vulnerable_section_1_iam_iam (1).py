 #!/usr/bin/env python3
 import threading
import ldap
 import os
 import sqlite3
 import threading
     l = ldap.initialize(ldap_url)
     l.simple_bind_s(settings.LDAP_IAM_USER, settings.LDAP_IAM_PASS)
     base = ','.join(['cn=users'] + settings.LDAP_BASE)
    res = l.search_s(base, ldap.SCOPE_SUBTREE, 'sAMAccountName=' + username, ['displayName'])
     name = ''
     if res:
         cn, d = res[0]
     l = ldap.initialize(ldap_url)
     l.simple_bind_s(settings.LDAP_IAM_USER, settings.LDAP_IAM_PASS)
     base = ','.join(['cn=users'] + settings.LDAP_BASE)
    u = l.search_s(base, ldap.SCOPE_SUBTREE, 'sAMAccountName=' + username, ['sAMAccountName'])
     return len(u) > 0
 
 def ldap_login_check(username, password):