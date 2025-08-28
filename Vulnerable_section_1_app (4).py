 
 @app.route("/register")
 def register():
     return render_template("register.html")
 
 @app.route("/create", methods=["POST"])
 
 @app.route("/login", methods=["POST"])
 def login():
     username = request.form["username"]
     password = request.form["password"]
 
 
 @app.route("/logout", methods=["POST"])
 def logout():
     session.clear()
     return redirect("/")
 
     if request.method == "POST":
         if "user_id" not in session:
             return redirect("/login")
        
        if request.method == "POST":
            check_csrf()
 
         content = request.form["content"]
         selected_categories = [int(c) for c in request.form.getlist("categories")]