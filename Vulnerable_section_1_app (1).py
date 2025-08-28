 import functools
 
 import flask
 import markupsafe
         return f(*args, **kwargs)
     return wrapper
 
 @app.route("/", methods=["GET", "POST"])
 def index():
     if flask.request.method == "GET":
         posts = database.get_posts()
         return flask.render_template("index.html", posts=posts)
    elif flask.request.method == "POST":
         if "cancel" in flask.request.form:
             return flask.redirect("/")
         keyword = flask.request.form["keyword"]
 def register():
     if flask.request.method == "GET":
         return flask.render_template("register.html")
    elif flask.request.method == "POST":
         username = flask.request.form["username"]
         password1 = flask.request.form["password1"]
         password2 = flask.request.form["password2"]
 def login():
     if flask.request.method == "GET":
         return flask.render_template("login.html")
    elif flask.request.method == "POST":
         username = flask.request.form["username"]
         password = flask.request.form["password"]
         if not username or not password or len(username) > 20 or len(password) > 20:
         if pwhash and security.check_password_hash(pwhash, password):
             flask.session["id"] = usr["id"]
             flask.session["username"] = username
             return flask.redirect("/")
         flask.flash("VIRHE: Väärä käyttäjätunnus tai salasana")
         return flask.redirect("/login")
 def logout():
     flask.session.pop("id", None)
     flask.session.pop("username", None)
     return flask.redirect("/")
 
 @app.route("/user/<int:user_id>")
         flask.abort(403)
     if flask.request.method == "GET":
         return flask.render_template("delete_user.html", user_id=user_id)
    elif flask.request.method == "POST":
         if "yes" in flask.request.form:
             with database.dbase as db:
                 db.execute("DELETE FROM Users WHERE id = ?", [user_id], commit=True)
     if flask.request.method == "GET":
         classes = database.get_classes()
         return flask.render_template("new_post.html", classes=classes)
    elif flask.request.method == "POST":
         content = flask.request.form["content"]
         if not content or len(content) > 1000 or "class" not in flask.request.form:
             flask.abort(403)
     if flask.request.method == "GET":
         classes = database.get_classes()
         return flask.render_template("edit_post.html", post=post, classes=classes)
    elif flask.request.method == "POST":
         content = flask.request.form["content"]
         if not content or len(content) > 1000 or "class" not in flask.request.form:
             flask.abort(403)
         flask.abort(403)
     if flask.request.method == "GET":
         return flask.render_template("delete_post.html", post_id=post_id)
    elif flask.request.method == "POST":
         if "yes" in flask.request.form:
             with database.dbase as db:
                 db.execute("DELETE FROM Posts WHERE id = ?", [post_id], commit=True)
     if flask.request.method == "GET":
         cmmnts = database.get_comments(post_id=post_id)
         return flask.render_template("comments.html", post=post, comments=cmmnts)
    elif flask.request.method == "POST":
         if "cancel" in flask.request.form:
             return flask.redirect(f"/comments/{post_id}")
         keyword = flask.request.form["keyword"]
         flask.abort(404)
     if flask.request.method == "GET":
         return flask.render_template("new_comment.html", post_id=post_id)
    elif flask.request.method == "POST":
         content = flask.request.form["content"]
         if not content or len(content) > 1000:
             flask.abort(403)
         flask.abort(403)
     if flask.request.method == "GET":
         return flask.render_template("edit_comment.html", comment=comment)
    elif flask.request.method == "POST":
         content = flask.request.form["content"]
         if not content or len(content) > 1000:
             flask.abort(403)
         flask.abort(403)
     if flask.request.method == "GET":
         return flask.render_template("delete_comment.html", comment_id=comment_id)
    elif flask.request.method == "POST":
         if "yes" in flask.request.form:
             with database.dbase as db:
                 db.execute("DELETE FROM Comments WHERE id = ?", [comment_id], commit=True)