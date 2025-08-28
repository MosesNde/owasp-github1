 
 def fetch_website(urllib_version, url):
     # Import the requested version (2 or 3) of urllib
    if urllib_version == 2 or urllib_version == 3:
        exec(f"import urllib{urllib_version} as urllib", globals())
     else:
        print("wrong version")
        return None
     
     # Fetch and print the requested URL
     try: 
         http = urllib.PoolManager()
         r = http.request('GET', url)
     except:
         print('Exception')
 
 
 def load_yaml(filename):