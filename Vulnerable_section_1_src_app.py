         not request.path.startswith("/a/")
     ):
         return redirect("/reset-password")
 
 # MARK: Pages
 @app.route("/")