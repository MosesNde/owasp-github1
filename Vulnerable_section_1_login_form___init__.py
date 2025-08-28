 import os
 from flask import Flask
 
 def create_app(test_config=None):
     # create and configure the app
     app = Flask(__name__, instance_relative_config=True)
     app.config.from_mapping(
         SECRET_KEY='super_secret_key',
         DATABASE=os.path.join(app.instance_path, 'login_form.sqlite'),