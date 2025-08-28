         self.assertStatus('303 See Other')
         self.assertHeaderItemValue("Location", self.baseurl + "/dnszone/")
 
     def test_login_with_redirect_query_string(self):
         # Given a user redirected to login page with a query string.
         # When trying to login
         self.assertStatus("200 OK")
         self.assertInBody('value="/dnszone/"')
 
     def test_login_invalid_credentials(self):
         # Given invalid credentials.
         username = "myusername"
         self.getPage("/")
         # Then user is redirected to login page.
         self.assertStatus('303 See Other')
        self.assertHeaderItemValue('Location', self.baseurl + '/login/?redirect=%2F')
 
     def test_redirect_to_login_with_url(self):
         # When trying to access a proptected page.
         self.getPage("/dnszone/")
         # Then user is redirected to login page.
         self.assertStatus('303 See Other')
         self.assertHeaderItemValue('Location', self.baseurl + '/login/?redirect=%2Fdnszone%2F')