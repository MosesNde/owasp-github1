 from flask.globals import session
 from flask_sqlalchemy import SQLAlchemy
 from flask import send_file
 import os
 app = Flask(__name__)
 app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
 @app.route('/link')
 def link():
     link = request.args.get('link')
    return redirect(link)
 
 if __name__ == "__main__":
     app.run(debug=True)
\ No newline at end of file