         redirect = cherrypy.serving.request.path_info
         query_string = cherrypy.serving.request.query_string
         if query_string:
            redirect = redirect + '?' + query_string
        new_url = cherrypy.url(login_url, qs={'redirect': redirect})
         raise cherrypy.HTTPRedirect(new_url)
 
 