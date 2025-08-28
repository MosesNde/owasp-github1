     if request.method == "POST":
         if "file" not in request.files:
             flash("No file part")
            return redirect(request.url)
 
         file = request.files["file"]
         if file.filename is None or file.filename == "":
             flash("No selected file")
            return redirect(request.url)
 
         if not file_is_allowed_to_upload(file.filename):
             flash(f'"{file.filename}" is not allowed to upload')
            return redirect(request.url)
 
         filename = secure_filename(file.filename)
         if filename != file.filename:
             current_app.logger.warning('filename is sanitized to: "%s"', filename)
 
         file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for("file_upload.upload_completed"))
 
     return render_template("file_upload.html")
 