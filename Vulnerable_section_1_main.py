 from markupsafe import escape
 import os
 import subprocess
 
 
 app = Flask(__name__, template_folder='templates')
 @app.route('/read_file', methods=['POST'])
 def read_file():
     filename = request.form.get('filename')
    filepath = os.path.join('uploads', filename)

    try:
        with open(filepath, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        return str(e)
 
 ### OS command injection
 