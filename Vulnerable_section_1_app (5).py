 recaptcha.init_app(app)
 
 num = [str(i) for i in range(10)]
alpha = 
allow = []
 
 @app.route('/', methods = ['GET', 'POST'])
 def index():
         if recaptcha.verify():
             url = request.form.get('url')
             new_url = request.form.get('new-url')
             if new_url in popen("ls ../s").read().split('\n'):
                 return 'this url has been occurpied...<a href="/">back home</a>'
 