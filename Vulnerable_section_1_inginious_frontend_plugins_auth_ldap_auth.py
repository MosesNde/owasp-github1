 
 from flask import redirect
 from ldap3.core.exceptions import LDAPException
 
 from inginious.frontend.pages.social import AuthenticationPage
 from inginious.frontend.user_manager import AuthMethod
         attr_cn = settings.get("cn", "cn")
         attr_mail = settings.get("mail", "mail")
         try:
            ldap_request = settings["request"].format(login)
             conn.search(settings["base_dn"], ldap_request, attributes=[attr_cn, attr_mail])
             user_data = conn.response[0]
         except (LDAPException, IndexError) as ex: