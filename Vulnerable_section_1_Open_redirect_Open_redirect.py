 
 init(autoreset=True)
 
TIMEOUT = 5  # Timeout in seconds
 
 # Common redirect parameters
 redirect_params = [
     return filtered
 
 # Function to test URL with a given payload
def test_redirect(bug_path ,url, payload, log_file):
     try:
         parsed_url = urllib.parse.urlparse(url)
         query_params = urllib.parse.parse_qs(parsed_url.query)
             # Create tasks for each URL and payload combination
             for url in urls:
                 for payload in payloads:
                    executor.submit(test_redirect, bug_path, url, payload, log_file)
 
 # Main function
 def open_redirect(bug_path, target):