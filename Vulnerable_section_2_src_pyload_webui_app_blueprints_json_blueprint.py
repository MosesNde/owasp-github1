 def edit_package():
     api = flask.current_app.config["PYLOAD_API"]
     try:
        id = int(flask.request.form["pack_id"])
         data = {
             "name": flask.request.form["pack_name"],
            "_folder": flask.request.form["pack_folder"],
             "password": flask.request.form["pack_pws"],
         }
 
        api.set_package_data(id, data)
         return jsonify(response="success")
 
     except Exception: