             return redirect(url_for('index'))
 
     target = request.args.get('target')
     if target and len(target) > 0:
        return redirect(target)
     return render_template('auth/login.html')
 
 @bp.before_app_request
 def load_logged_in_user():
     user_id = session.get('user_id')