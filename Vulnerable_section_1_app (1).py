         username = request.form['username']
         password = request.form['password']
 
        # SQL Injection vulnerability: Directly embedding user input into the query
         conn = sqlite3.connect('users.db')
         cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("Executing query:", query)  # For demonstration purposes
        cursor.execute(query)
         user = cursor.fetchone()
         conn.close()
 