             # return render_template('login.html', form=form)
             return redirect(url_for("auth.login"))
         target = request.args.get("target")
        if target is not None:
             logger.info(("Login redirect:", target))
             return redirect(target)
         return redirect(url_for("index.index"))
         DataRequired(),
         Regexp("^(0|[1-9][0-9]*){1}(\.[0-9]{2})?$", message="Invalid input.")
     ])
\ No newline at end of file