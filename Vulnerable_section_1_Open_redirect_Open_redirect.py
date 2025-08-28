 import urllib.parse
 from Start_up.remove_file import delete_empty_text_files
 from colorama import Fore, Style, init
 
 init(autoreset=True)
 
     return filtered
 
 # Function to test URL with a given payload
def test_redirect(bug_path ,url, payload):
     try:
         parsed_url = urllib.parse.urlparse(url)
         query_params = urllib.parse.parse_qs(parsed_url.query)
        with open(f'{bug_path}/LOGS.txt', 'a') as f:
         # Test query-based injection
            for param in query_params:
                if param in redirect_params:
                    try:
                        response = requests.get(injected_url, allow_redirects=False, timeout=TIMEOUT)
                        print(f"\n{Fore.GREEN}[QUERY] {injected_url} -> {response.status_code}")
                        f.write(f"\n{Fore.GREEN}[QUERY] {injected_url} -> {response.status_code}")
                    except requests.exceptions.RequestException as req_err:
                        print(f"\n{Fore.RED}[ERROR] Timeout or request failed for {injected_url}: {str(req_err)}")
 
         # Test path-based injection
            for path in redirect_paths:
                if path in url:
                    injected_url = url.rstrip("/") + "/" + urllib.parse.quote_plus(payload)
                    try:
                        response = requests.get(injected_url, allow_redirects=False, timeout=TIMEOUT)
                        print(f"\n{Fore.GREEN}[PATH] {injected_url} -> {response.status_code}")
                        f.write(f"\n{Fore.GREEN}[PATH] {injected_url} -> {response.status_code}")
                    except requests.exceptions.RequestException as req_err:
                        print(f"\n{Fore.RED}[ERROR] Timeout or request failed for {injected_url}: {str(req_err)}")

     except Exception as e:
        print(f"\n{Fore.RED}[ERROR] {url}: {str(e)}")
 
# Function to start scanning with threading
 def scan_urls(bug_path, urls, payloads):
    threads = []
    for url in urls:
        for payload in payloads:
            thread = threading.Thread(target=test_redirect, args=(bug_path, url, payload))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
 
 # Main function
 def open_redirect(bug_path, target):
     input_file = f"{bug_path}/URL_FOR_{target}.txt"
     script_dir = os.path.dirname(os.path.abspath(__file__))
     file_path = os.path.join(script_dir, "payloads.txt")
     # Read URLs and payloads from files
     try:
         with open(input_file, "r") as f:
             urls = [line.strip() for line in f.readlines()]
     except FileNotFoundError:
         print(f"{Fore.RED}[-] Input file {input_file} not found!{Style.RESET_ALL}")
         return
     try:
         with open(file_path, "r") as f:
             payloads = [line.strip() for line in f.readlines()]
     except FileNotFoundError:
        print(f"{Fore.RED}[-] Payloads fIle at path {file_path} is not found!{Style.RESET_ALL}")
         return
 
     # Filter relevant URLs
     filtered_urls = filter_urls(urls)
     print(f"{Fore.BLUE}Filtered {len(filtered_urls)} potential redirect URLs from {len(urls)} total URLs.")
 
     # Scan for open redirects
    scan_urls(bug_path,filtered_urls, payloads)
    delete_empty_text_files(bug_path)
\ No newline at end of file