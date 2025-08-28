 import logging
 import re
 import socket
import subprocess
 from ipaddress import IPv4Network
 
 import requests
 		response = {}
 		response['status'] = False
 
 		wafw00f_command = f'wafw00f {url}'
		output = subprocess.check_output(wafw00f_command, shell=True)
		# use regex to get the waf
		regex = "behind \\\\x1b\[1;96m(.*)\\\\x1b"
		group = re.search(regex, str(output))

 		if group:
 			response['status'] = True
 			response['results'] = group.group(1)
 		url = req.query_params.get('url')
 		#save_db = True if 'save_db' in req.query_params else False
 		response = {'status': False}
 		try:
 			# response = get_cms_details(url)
 			response = {}