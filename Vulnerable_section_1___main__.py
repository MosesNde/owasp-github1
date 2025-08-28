 				"logSetting", "factoryReset", "reboot", "files", "datetime"
 			)
 
	if not cherrypy.session.get('USERNAME', None):
 		url = cherrypy.url().split('/')[-1]
 		if url and ".html" not in url and ".js" not in url and any(path in url for path in paths):
 			raise cherrypy.HTTPError(401)