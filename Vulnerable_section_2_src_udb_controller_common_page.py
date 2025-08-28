         }
 
     @cherrypy.expose
    def status(self, status, key, **kwargs):
         """
         Soft-delete the record.
         """
         self._verify_role(self.edit_role)
         obj = self._get_or_404(key)
         try:
         }
 
     @cherrypy.expose
    def follow(self, user_id, key, **kwargs):
         """
         Add current user to the list of followers.
         """
         self._verify_role(self.list_role)
         obj = self._get_or_404(key)
         userobj = User.query.filter_by(id=user_id).first()
         raise cherrypy.HTTPRedirect(url_for(obj, 'edit'))
 
     @cherrypy.expose
    def unfollow(self, user_id, key, **kwargs):
         """
         Add current user to the list of followers.
         """
         self._verify_role(self.list_role)
         obj = self._get_or_404(key)
         userobj = User.query.filter_by(id=user_id).first()