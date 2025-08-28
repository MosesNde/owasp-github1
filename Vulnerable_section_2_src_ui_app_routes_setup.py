 from itertools import chain
 from os import environ, getenv
 
 # from secrets import choice
 # from string import ascii_letters, digits
from threading import Thread
from time import time
 
 from flask import Blueprint, Response, flash, redirect, render_template, request, url_for
 from flask_login import current_user
 from app.dependencies import BW_CONFIG, DATA, DB
 from app.utils import LOGGER, USER_PASSWORD_RX, gen_password_hash
 
from app.routes.utils import REVERSE_PROXY_PATH, handle_error, manage_bunkerweb
 
 setup = Blueprint("setup", __name__)
 
 
             LOGGER.debug(f"Creating new service with base_config: {base_config} and config: {config}")
 
            operation, error = BW_CONFIG.new_service(base_config, override_method="wizard")
             if error:
                 return handle_error(f"Couldn't create the new service: {operation}", "setup", False, "error")
 
            # deepcode ignore MissingAPI: We don't need to check to wait for the thread to finish
            Thread(
                target=manage_bunkerweb,
                name="Reloading instances",
                args=("services", config | base_config, request.form["server_name"], request.form["server_name"]),
                kwargs={"operation": "edit", "threaded": True},
            ).start()
 
         return Response(status=200)
 
     if current_user.is_authenticated:
         return redirect(url_for("home.home_page"))
 
    if DB.get_ui_user():
        db_config = BW_CONFIG.get_config(methods=False, filtered_settings=("SERVER_NAME", "USE_UI", "REVERSE_PROXY_URL"))
        for server_name in db_config["SERVER_NAME"].split(" "):
            if server_name and db_config.get(f"{server_name}_USE_UI", db_config.get("USE_UI", "no")) == "yes":
                 return redirect(url_for("login.login_page"), 301)
 
     target_endpoint = request.args.get("target_endpoint", "")
     return render_template(
         "loading.html",
         message="Setting up Web UI...",