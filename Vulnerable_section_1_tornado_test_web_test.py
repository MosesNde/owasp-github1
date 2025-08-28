         # This test verifies that the open redirect that affected some configurations
         # prior to Tornado 6.3.2 is no longer possible. The vulnerability required
         # a static_url_prefix of "/" and a default_filename (any value) to be set.
        # The absolute server-side path to the static directory must also be known.
         with ExpectLog(gen_log, ".*cannot redirect path with two initial slashes"):
             response = self.fetch(
                f"//evil.com/../{os.path.dirname(__file__)}/static/dir",
                 follow_redirects=False,
             )
         self.assertEqual(response.code, 403)