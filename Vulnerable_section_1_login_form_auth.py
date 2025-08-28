 def index():
     return render_template('index.html')
 
 @bp.route('/register', methods=('GET', 'POST'))
 def register():
     if request.method == 'POST':
         username = request.form['username']
         password = request.form['password']
 
         error = None

         if not username:
             error = 'Username is required.'

         if error is None:
            User.create(username, password)
            return redirect(url_for('auth.login'))

         flash(error)
 
     return render_template('register.html')