 import json
 import logging

import flask
 from flask import Flask, render_template, request, redirect, url_for
 from datetime import date
from src import dbdata, webwork
 from src.connection import dbconnector
from flask_wtf.csrf import CSRFProtect
 
 # create flask app
 app = Flask(__name__, static_url_path='/static')
csrf = CSRFProtect()
csrf.init_app(app)
 UserID = 0
 
 