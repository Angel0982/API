
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost/nombre_basededatos'  # Cambia esto según tu configuración

db = SQLAlchemy(app)
#import os

#from app import create_app

#settings_module = os.getenv('APP_SETTINGS_MODULE')
#app = create_app(settings_module)

