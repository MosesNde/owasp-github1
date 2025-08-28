     return send_file('tournament-scheduler/build/index.html')
 
 
@app.route('/', methods=["GET", "POST"])
 def index():
     return redirect(url_for('global_scoreboard'))
 