 @app.context_processor
 def inject_variables():
     current_endpoint = request.path.split("/")[-1]
    if request.path.startswith(("/check_reloading", "/setup", "/loading", "/login", "/totp")):
         return dict(current_endpoint=current_endpoint, script_nonce=app.config["SCRIPT_NONCE"])
 
     DATA.load_from_file()
 
         DB.readonly = DATA.get("READONLY_MODE", False)
 
        if not request.path.startswith(("/check_reloading", "/loading", "/login", "/totp")) and DB.readonly:
             flask_flash("Database connection is in read-only mode : no modifications possible.", "error")
 
         if current_user.is_authenticated:
 ### * MISC ROUTES * ###
 
 
@app.route("/", strict_slashes=False)
 def index():
     if DB.get_ui_user():
         if current_user.is_authenticated:  # type: ignore
     return redirect(url_for("setup.setup_page"), 301)
 
 
@app.route("/loading")
 @login_required
 def loading():
    return render_template(
        "loading.html", message=request.values.get("message", "Loading..."), next=request.values.get("next", None) or url_for("home.home_page")
    )
 
 
 @app.route("/check", methods=["GET"])
     return Response(status=200, headers={"Access-Control-Allow-Origin": "*"}, response=dumps({"message": "ok"}), content_type="application/json")
 
 
@app.route("/check_reloading")
 @login_required
 def check_reloading():
     DATA.load_from_file()