 
     if name:
         cursor.execute(
            "SELECT * FROM books WHERE name LIKE '%" + name + "%'"
         )
         books = [Book(*row) for row in cursor]
 
     elif author:
         cursor.execute(
            "SELECT * FROM books WHERE author LIKE '%" + author + "%'"
         )
         books = [Book(*row) for row in cursor]
 