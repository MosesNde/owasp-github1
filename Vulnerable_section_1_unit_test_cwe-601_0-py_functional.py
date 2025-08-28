                     client = app.test_client()
                     
                     def test_logic():
                        response = client.get(f"/?target=http://localhost/test")
                         self.assertEqual(response.status_code, 302)
                        self.assertEqual(response.location, 'http://localhost/test')
 
                     try:
                         func_timeout(timeout_duration, test_logic)