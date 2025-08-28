 from flask import render_template, request, redirect, url_for, flash, jsonify, session
 from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
 from werkzeug.utils import secure_filename
 from app import app, db
 from models import User, FarmerProfile, CustomerProfile
             # Set JWT token in session
             session['token'] = access_token
             
             # Redirect based on user type
             if user.user_type == 'farmer':
                 flash('Login successful!', 'success')