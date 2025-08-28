 import sqlite3
 import os
 
 #exec(open('db_maker.py').read())
 
 app = Flask(__name__)
 def load_image():
     filename = request.args.get('filename')
     if filename:
        filepath = './static/images/' + filename
        return send_file(filepath)
     else:
         return 'Файл не найден', 404
 