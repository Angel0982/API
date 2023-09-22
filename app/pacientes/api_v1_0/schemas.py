from marshmallow import fields

from app.ext import ma
from app.db import db, BaseModelMixin
import datetime

class PacienteSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(200))
    fecha_ingreso = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    estado = db.Column(db.String(20), default='En tratamiento')
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)


class DoctorSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    contact_number = db.Column(db.String(15))
    email = db.Column(db.String(100))
    #hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)

class EnfermeroSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer)
    especialidad = db.Column(db.String(100))
    fecha_contratacion = db.Column(db.Date)
    salario = db.Column(db.Float)

class CamilleroSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    telefono = db.Column(db.String(15))
    fecha_contratacion = db.Column(db.Date)
    activo = db.Column(db.Boolean)
    
class VigilanteSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    turno = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)