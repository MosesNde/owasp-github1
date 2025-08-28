             return False
 
     def checkPassword(self, username, password):
        if self.check_username(username):
             self.cursor.execute(
                 f"select password from users where username = '{username}'")
             dbResult = self.cursor.fetchall()