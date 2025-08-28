 def fetch_website(urllib_version, url):
     # Import the requested version (2 or 3) of urllib
     if urlib_version == '3.00':
        exec(f"import urllib{urllib_version} as urllib", globals())
     # Fetch and print the requested URL
 
     try: