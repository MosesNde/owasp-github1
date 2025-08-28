             )
         return ''
 
    def get_full_path(self, filename, language=None, version_slug=None):
         """
         Return a full path for a given filename.
 
         This will include version and language information. No protocol/domain
         is returned.
         """
         # Handle explicit http redirects
        if re.match('^https?://', filename):
             return filename
 
         return resolve_path(
         if path.startswith(self.from_url):
             log.debug('Redirecting %s', self)
             cut_path = re.sub('^%s' % self.from_url, '', path)
             to = self.get_full_path(
                 filename=cut_path,
                 language=language,
                 version_slug=version_slug,
             )
             return to
 
                 filename=self.to_url.lstrip('/'),
                 language=language,
                 version_slug=version_slug,
             )
             return to
 
     def redirect_exact(self, path, language=None, version_slug=None):
         full_path = path
         if language and version_slug:
             # reconstruct the full path for an exact redirect
            full_path = self.get_full_path(path, language, version_slug)
         if full_path == self.from_url:
             log.debug('Redirecting %s', self)
             return self.to_url
                     filename=to,
                     language=language,
                     version_slug=version_slug,
                 )
 
     def redirect_sphinx_htmldir(self, path, language=None, version_slug=None):
                 filename=to,
                 language=language,
                 version_slug=version_slug,
             )