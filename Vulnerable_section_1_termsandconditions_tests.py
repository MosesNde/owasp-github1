         )
         self.assertContains(accept_version_post_response, "Secure")
 
    def test_accept_redirect_safe(self):
         # Pre-accept terms 2 and 3
         UserTermsAndConditions.objects.create(user=self.user1, terms=self.terms2)
         UserTermsAndConditions.objects.create(user=self.user1, terms=self.terms3)
 
         LOGGER.debug("Test /terms/accept/site-terms/1/ post")
         accept_response = self.client.post(
            "/terms/accept/", {"terms": 1, "returnTo": "/secure/"}, follow=True
         )
         self.assertRedirects(accept_response, "/secure/")
 
     def test_accept_redirect_unsafe(self):
        # Pre-accept terms 2 and 3
        UserTermsAndConditions.objects.create(user=self.user1, terms=self.terms2)
        UserTermsAndConditions.objects.create(user=self.user1, terms=self.terms3)
 
        LOGGER.debug("Test /terms/accept/contrib-terms/3/ post")
        accept_response = self.client.post(
            "/terms/accept/", {"terms": 3, "returnTo": "http://attacker/"}, follow=False
        )
         self.assertRedirects(accept_response, "/")
 
     def test_accept_store_ip_address(self):