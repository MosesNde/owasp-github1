         Raises:
             Exception: If there is an error executing the database query.
         """
        query = f"SELECT * FROM {self.table_user} WHERE username = '{username}';"
 
         if DEBUG_MODE:
             print(f"[DEBUG] {FILE_NAME}: get_user_by_username: {query} with username: {username}")
 
        self.cursor.execute(query)
         result = self.cursor.fetchone()
 
         if DEBUG_MODE: