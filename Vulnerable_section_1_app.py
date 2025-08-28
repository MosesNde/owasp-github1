 import logging
 from datetime import timedelta
 from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
 from flask_sqlalchemy import SQLAlchemy
 from sqlalchemy.orm import DeclarativeBase
 from werkzeug.middleware.proxy_fix import ProxyFix
 from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
 from flask_cors import CORS
 from werkzeug.utils import secure_filename
 import uuid
 import json
 # JWT configuration
 app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "jwt-dev-secret")
 app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
 jwt = JWTManager(app)
 
 # CORS configuration
 CORS(app)
 