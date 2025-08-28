 def page_not_found_error(error):
     return render_template('error.html')
 
 @app.route('/api/user', methods = ['GET'])
 def evaluate():
     if session['logged_in']:
         data = request.args.get('user')
        return str(eval(data))
     else:
         return redirect('error.html')
  