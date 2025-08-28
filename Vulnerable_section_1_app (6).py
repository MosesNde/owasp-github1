 from flask import Flask, request, render_template, redirect, flash, jsonify, send_file
 from flask_debugtoolbar import DebugToolbarExtension
 from flask_cors import CORS
 from models import db, connect_db, System, Object, AltName
 from functions import get_obj_batch, get_obj_vectors, get_id_list
 @app.route('/images/<path:img_path>')
 def get_image(img_path):
     """Returns the image file located at the given path"""
    return send_file(f'images/{img_path}')