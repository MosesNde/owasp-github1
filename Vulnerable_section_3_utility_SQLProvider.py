         except mysql.connector.Error:
             print("Database {} does not exists.".format(dbName))
 
    def insert(self, prompt: str, returnedValue: str | None = None) -> int | None:
         """Permits to execute INSERT and UPDATE statements"""
         try:
            self.cursor.execute(prompt + ("RETURNING {}".format(returnedValue) if returnedValue else ""))
             self.cnx.commit()
             if self.connectionType == 'online' and returnedValue:
                 return self.cursor.fetchone()[0]
             return self.cursor.lastrowid
         except mysql.connector.Error as err:
             print(err)
 
    def get(self, prompt: str):
         """Permits to execute SELECT statements"""
         try:
            self.cursor.execute(prompt)
             response = self.cursor.fetchall()
             return response
         except mysql.connector.Error as err:
             print(err)
 
    def executeSQL(self, prompt: str):
         try:
            self.cursor.execute(prompt)
             self.cnx.commit()
         except mysql.connector.Error as err:
             print(err)