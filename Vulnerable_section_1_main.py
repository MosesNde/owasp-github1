 from flask import Flask, request, render_template, redirect, make_response
 import sqlite3
 import time
 from markupsafe import escape
 import os
 import subprocess
 @app.route('/execute', methods=['POST'])
 def execute():
     command = request.form.get('command')
    return subprocess.check_output(command, shell=True)
 
 if __name__ == "__main__":
     app.run(debug=True)