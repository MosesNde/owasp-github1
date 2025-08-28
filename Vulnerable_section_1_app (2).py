 from flask import Flask, render_template, request, redirect, session
from flask_wtf.csrf import CSRFProtect

 import csv
 import os
 
 app = Flask(__name__)
app.secret_key = 'your-secret-key'
 csrf = CSRFProtect(app)
 OPTIONS_FILE = 'options.txt'
 VOTE_FILE = 'votes.csv'
 STATUS_FILE = 'status.txt'
 TITLE_FILE = 'title.txt'
 CONFIG_FILE = 'vote_config.txt'
 
 def get_vote_status():
     if not os.path.exists(STATUS_FILE):
                            session_id=config['session_id'])
 
 if __name__ == '__main__':
    app.run(debug=True)