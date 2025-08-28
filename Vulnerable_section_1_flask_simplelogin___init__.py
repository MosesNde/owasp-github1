 import os
 from functools import wraps
 from uuid import uuid4
 from warnings import warn
 
 from flask import (
     Blueprint,
     current_app,
     flash,
             default=request.form.get("next", default=self.config.get("home_url", "/")),
         )
 
         if is_logged_in():
             self.flash_message("is_logged_in")
             return redirect(destiny)