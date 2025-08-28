 def login():
     """Log in a registered user by adding the user id to the session."""
     if request.method == "POST":
        target = request.args.get('target')
        if target is not None:
            return redirect(target)
         request_username = request.form["username"]
         request_password = request.form["password"]
 