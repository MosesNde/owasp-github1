 
 from io import open
 from ldap3 import Server, Connection, ALL
from ldap3.utils.dn import escape_rdn
 from flask import request
 from sqlalchemy import exc
 from sqlalchemy.orm import sessionmaker
 
     # Look for the user entry.
     if not c.search(config.LDAPBASE,
                    "(" + config.LDAPFIELD + "=" + escape_rdn(login) + ")") :
         app.logger.error("Error: Connection to the LDAP with service account failed")
     else:
         if len(c.entries) >= 1 :
     s = Server(config.LDAPURI, port=config.LDAPPORT,
                use_ssl=False, get_info=ALL)
     # 1. connection with service account to find the user uid
    uid = useruid(s, escape_rdn(login))
    
     if uid: 
         # 2. Try to bind the user to the LDAP