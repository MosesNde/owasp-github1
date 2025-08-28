 
 @blueprint.route("/__weave/file/<path:path>")
 def send_local_file(path):
    # path is given relative to the FS root. check to see that path is a subdirectory of the
    # local artifacts path. if not, return 403. then if there is a cache scope function defined
    # call it to make sure we have access to the path
    abspath = (
        "/" / pathlib.Path(path)
    )  # add preceding slash as werkzeug strips this by default and it is reappended below in send_from_directory
     try:
        local_artifacts_path = pathlib.Path(filesystem.get_filesystem_dir()).absolute()
    except errors.WeaveAccessDeniedError:
        abort(403)
    if local_artifacts_path not in list(abspath.parents):
         abort(403)
    return send_from_directory("/", path)
 
 
 @blueprint.before_request