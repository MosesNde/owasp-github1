 import yaml
 import flask
 
 APP = flask.Flask(__name__)
 
 
 def fetch_website(urllib_version, url):
     # Import the requested version (2 or 3) of urllib
     exec(f"import urllib{urllib_version} as urllib", globals())
     # Fetch and print the requested URL
  