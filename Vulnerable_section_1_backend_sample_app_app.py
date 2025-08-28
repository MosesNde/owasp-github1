 import json.decoder
 
from flask import Flask, Response, jsonify, flash, request, render_template, redirect
 from flask_login import LoginManager, login_user, logout_user, current_user, login_required
 from werkzeug.security import check_password_hash, generate_password_hash
 
 import const
 import os
 import re
 
 app = Flask(__name__, static_folder='static')
 app.config.from_object('config')
 csrf = CSRFProtect(app)
 
 init_db(app)
 
     if request.method == "GET":
         user = User.query.filter_by(id=user_id).first()
         return render_template('users/edit.html', user=user)
 
     elif request.method == "POST":
         return redirect(f'/users/{user_id}')
 
 
 @app.route('/users/<int:user_id>/report', methods=['POST'])
 @login_required
 def report(user_id):
             flash('Login failed...')
             return render_template('login.html')
     else:
        redirect_url = request.args.get('redirect')
        if not redirect_url:
            redirect_url = '/'

         if current_user.is_authenticated:
            return redirect(redirect_url)
 
        return render_template('login.html', redirect_url=redirect_url)
 
 
 @app.route('/logout', methods=['GET'])
 @app.route('/debug', methods=['GET', 'POST'])
 @csrf.exempt
 def debug():
    callback = request.args.get('callback')

     headers = {}
     for header in request.headers:
         headers[header[0]] = header[1]
 
    if callback:
        return jsonp(callback, headers)

     return jsonify(body=request.form, headers=headers)
 
 
def jsonp(callback, headers):
    return Response(
        f'{callback}({jsonify(body=request.form, headers=headers).data.decode()});',
        mimetype="text/javascript"
        )

 @login_manager.unauthorized_handler
 def unauthorized():
    return redirect(f'/login?redirect={request.path}')
 
 
 if __name__ == '__main__':