                 )
 
         try:
            query = f"SELECT * FROM users WHERE username = '{username}' AND password_hash = '{password}'"
            result = db.session.execute(query)
             user_data = result.fetchone()
 
             if user_data: