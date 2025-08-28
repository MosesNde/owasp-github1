 		netlas_key = get_netlas_key()
 		command += f' -a {netlas_key}' if netlas_key else ''
 
		result = subprocess.check_output(command.split()).decode('utf-8')
 		if 'Failed to parse response data' in result:
 			# do fallback
 			return {