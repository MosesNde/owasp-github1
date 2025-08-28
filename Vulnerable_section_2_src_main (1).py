 import json
 import logging
 from flask import Flask, render_template, request, redirect, url_for
 from datetime import date
from src import dbdata, tablegenerator, formatprices, webwork
 from src.connection import dbconnector
 
 # create flask app
 app = Flask(__name__, static_url_path='/static')
 UserID = 0
 
 