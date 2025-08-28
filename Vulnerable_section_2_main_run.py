 from authlib.integrations.flask_client import OAuth
 from six.moves.urllib.parse import urlencode
 

 #----------------------------------------------------------------------------#
 # App Config.
 #----------------------------------------------------------------------------#
         self.status_code = status_code
 
 
 def check_permissions(permission, payload):
     if 'permissions' not in payload:
                         raise AuthError({
         }, 403)
     return True
 

 def requires_auth(permission=''):
   def requires_auth_decorator(f):
     @wraps(f)
     def decorated(*args, **kwargs):
       if 'profile' not in session:
         # Redirect to Login page here
         return redirect('/login')

       check_permissions(permission, payload)
 
       return f(*args, **kwargs)