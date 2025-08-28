     return export_params_json, html
 
 def sanitize_input(user_input):
    return re.sub(r'[\r\n]', '', user_input).strip()
 
 def start_server(port):
     http_server = WSGIServer(("localhost", port), app)