         r = self.client.get('/en/latest/redirect/', HTTP_HOST='pip.readthedocs.org')
         self.assertEqual(r.status_code, 404)
 
     @override_settings(USE_SUBDOMAIN=True)
     def test_redirect_root(self):
         Redirect.objects.create(
         self.redirect = get(Redirect, project=self.proj)
 
     def test_http_filenames_return_themselves(self):
         self.assertEqual(
             self.redirect.get_full_path('http://rtfd.org'),
             'http://rtfd.org',
         )
 