
 from flask import request, render_template, make_response
 
 from server.webapp import flaskapp, cursor
 
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
 