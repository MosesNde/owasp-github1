         logging.info('Getting CSRF token')
         self.driver.get('https://www.paypal.com/myaccount/transactions/')
         # Get CSRF token
        body_element, = self.wait_and_locate((By.ID, "__APP_DATA__"))
        data = base64.b64decode(body_element.get_attribute("innerHTML"))
         attribute_object = json.loads(data)
         self.csrf_token = attribute_object["_csrf"]
         return self.csrf_token
 
     def get_transaction_list(self):