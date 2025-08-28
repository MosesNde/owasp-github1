 # views.py

 from io import BytesIO
 from json import dumps
 from typing import Any
 from flask_login import current_user
 from flask import (
     Blueprint,
     Response,
     # Prevent from other users to access
     user = User.query.filter_by(username=username).first()
     if (user is not None) and (user.image_data is not None):
        return send_file(BytesIO(user.image_data), mimetype="image/jpeg")
 
     return safe_send_default_image()
 