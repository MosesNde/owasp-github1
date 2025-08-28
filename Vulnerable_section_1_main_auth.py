 from functools import wraps
 from jose import jwt
 from urllib.request import urlopen
from main import app
 
# app instance running in __init__.py
# app = Flask(__name__)
 
 AUTH0_DOMAIN = 'jjlovaglio.us.auth0.com'
 # AUTH0_DOMAIN = os.environ['AUTH0_DOMAIN']
     return wrapper
 
 
@app.route('/headers')
@requires_auth
def headers(payload):
    print(payload)
    return 'Access Granted'
 
if __name__ == '__main__':
    app.run()
\ No newline at end of file