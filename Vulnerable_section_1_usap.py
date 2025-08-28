     if dmp_link.startswith('/'):
         dmp_link = dmp_link[1:]
     try:
         return send_file(os.path.join(current_app.root_path, dmp_link),
                          attachment_filename=os.path.basename(dmp_link))
     except:
         return redirect(url_for('not_found'))
 
 
 def get_project(project_id):
     if project_id is None:
         return None