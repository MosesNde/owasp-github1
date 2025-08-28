 	proxy = get_random_proxy()
 
 	if proxy:
		httpx_command += " --http-proxy '{}' ".format(proxy)
 
 	if CUSTOM_HEADER in yaml_configuration and yaml_configuration[CUSTOM_HEADER]:
 		httpx_command += ' -H "{}" '.format(yaml_configuration[CUSTOM_HEADER])
 
	httpx_command += ' -json -o {} '.format(
		httpx_results_file
 	)
	httpx_command = 'cat {} | {}'.format(subdomain_scan_results_file, httpx_command)
	print(httpx_command)
	os.system(httpx_command)
 
 	# alive subdomains from httpx
 	alive_file = open(alive_file_location, 'w')
 
 	logger.info(eyewitness_command)
 
	os.system(eyewitness_command)
 
 	if os.path.isfile(result_csv_path):
 		logger.info('Gathering Eyewitness results')
 
 	# run naabu
 	logger.info(naabu_command)
	os.system(naabu_command)
 
 	# writing port results
 	try: