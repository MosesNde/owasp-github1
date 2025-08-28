         if not match:
             flask.abort(404)
         relpath = match.relative_to(base_path)
         ## print(f" [TRACE] relpath = {path} ; match = {match}")
         resp = None
         ###  Render org-mode file 