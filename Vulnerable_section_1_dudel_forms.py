 from wtforms.validators import Required, Length, Regexp, Optional, NoneOf
 from dudel.models import Poll, update_user_data
 import ldap
 
 # Helper class for multiple forms on one page
 class MultiForm(Form):
             # At this point, we update the user info (since we already have
             # a connection to LDAP)
             #connection.start_tls_s()
            connection.simple_bind_s(app.config["LDAP_DN"] % username, field.data)
             filter = app.config["LDAP_FILTER"] % "13demo1"
             results = connection.search_s(app.config["LDAP_BASEDN"], ldap.SCOPE_SUBTREE, filter)
             results = {k:(v if len(v)>1 else v[0]) for k,v in results[0][1].iteritems()}