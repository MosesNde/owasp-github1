 app.secret_key=config.secret_key
 
 def check_csrf():
    if "csfr_token" not in request.form:
         abort(403)
     if request.form["csrf_token"] != session["csrf_token"]:
         abort(403)
         if user_id:
             session["user_id"] = user_id
             session["username"] = username
            session["csfr_token"] = secrets.token_hex(16)
             return redirect("/")
         else:
             flash ("VIRHE: Väärä käyttäjätunnus tai salasana", "error")