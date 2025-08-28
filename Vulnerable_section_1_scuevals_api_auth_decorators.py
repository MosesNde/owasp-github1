 from functools import wraps
 from flask_jwt_extended import get_jwt_identity, jwt_required, current_user
 from werkzeug.exceptions import Unauthorized
 
 from scuevals_api.models import User
     @wraps(fn)
     def wrapper(*args, **kwargs):
 
        jwt_required(lambda: None)()
 
         identity = get_jwt_identity()
 