 from flask import Flask
 from flask import abort, flash, redirect, render_template, request, session
 from functools import wraps
 import config
 import db
import groups, users
 
 app = Flask(__name__)
 app.secret_key = config.secret_key
         return f(*args, **kwargs)
     return decorated_function
 
 @app.route("/")
 def index():
     return render_template("index.html")
 
         session["username"] = username
         session["user_id"] = user_id
         return redirect("/")
 
 @app.route("/logout")
 def logout():
     if "user_id" in session:
         del session["username"]
         del session["user_id"]
     return redirect("/")
 
 @app.route("/groups")
         return render_template("create_group.html")
 
     if request.method == "POST":
         group_name = request.form["group_name"]
         if not group_name or len(group_name) > 50:
             abort(403)
 @app.route("/update_group", methods=["POST"])
 @login_required
 def update_group():
     group_id = request.form["group_id"]
     group = groups.get_group(group_id)
     if not group:
 @app.route("/delete_group", methods=["POST"])
 @login_required
 def delete_group():
     group_id = request.form["group_id"]
     group = groups.get_group(group_id)
     if not group:
 @app.route("/join_group/group_id=<int:group_id>", methods=["POST"])
 @login_required
 def join_group(group_id):
     group_data = groups.get_group(group_id)
     if not group_data:
         abort(404)
 @app.route("/leave_group/group_id=<int:group_id>", methods=["POST"])
 @login_required
 def leave_group(group_id):
     group_data = groups.get_group(group_id)
     if not group_data:
         abort(404)