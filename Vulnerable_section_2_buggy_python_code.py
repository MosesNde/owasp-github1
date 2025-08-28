 
 
 def import_urlib_version(version):
    exec("import urllib%s as urllib" % version)
 
 
 @app.route('/')