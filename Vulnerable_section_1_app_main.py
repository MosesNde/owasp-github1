 import secrets
 from flask import Flask, request, g
 from flask_restx import Api, Resource, fields  # Asegúrate de tener instalada esta dependencia
 )
 
 app = Flask(__name__)
# Configura una clave secreta para el manejo de sesiones y tokens CSRF
app.config['SECRET_KEY'] = 'UAH9E/oqSWRm5bhne61DZZrzLFDU/hKDOD/djPPBfaW6VoGCc/0T5uYl2O61UE6P'
 
 # Inicializa la protección CSRF en la aplicación
 csrf = CSRFProtect(app)