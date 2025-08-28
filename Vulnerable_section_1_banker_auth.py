 from banker.db import get_db
 
 bp = Blueprint("auth", __name__, url_prefix="/auth")
 
 def login_required(view):
     """View decorator that redirects anonymous users to the login page."""
         if user:
             session.clear()
             session["user_id"] = user["id"]
            if target:
                 return redirect(target)
             else:
                 return redirect(url_for('bank.index'))