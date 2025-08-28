 @app.route('/user')
 def get_users():
     user = flask.request.args["user"]
    sql = """SELECT user FROM users WHERE user = \'%s\'"""
 
     conn = sqlite3.connect('example')
    conn.cursor().execute(sql % (user)) # Noncompliant
\ No newline at end of file
\ No newline at end of file