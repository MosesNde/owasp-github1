 import os
 from flask import Flask, request  
 
 ### Unrelated to the exercise -- Starts here -- Please ignore
 app = Flask(__name__)
         
         # builds path
         base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))
     
         with open(prof_picture_path, 'rb') as pic:
             picture = bytearray(pic.read())
         if not path:
             raise Exception("Error: Tax form is required for all users")
        
        with open(path, 'rb') as form:
             tax_data = bytearray(form.read())
 
         # assume that taxa data is returned on screen after this