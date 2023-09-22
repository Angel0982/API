#from operator import length_hint
#from sqlalchemy.orm import backref
from app.db import db, BaseModelMixin
import datetime


class Paciente(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(200))
    fecha_ingreso = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    estado = db.Column(db.String(20), default='En tratamiento')
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, nombre, edad, genero, direccion, usuario_id):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.usuario_id = usuario_id

    def __repr__(self):
        return f'Paciente({self.nombre}, {self.edad})'

    def __str__(self):
        return f'{self.nombre}, {self.edad}'


class Doctor(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    contact_number = db.Column(db.String(15))
    email = db.Column(db.String(100))
    #hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)

    def __init__(self, name, specialization, contact_number, email, hospital_id):
        self.name = name
        self.specialization = specialization
        self.contact_number = contact_number
        self.email = email
        self.hospital_id = hospital_id

    def __repr__(self):
        return f'Doctor({self.name}, {self.specialization})'

    def __str__(self):
        return f'{self.name}, {self.specialization}'


class Enfermero(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer)
    especialidad = db.Column(db.String(100))
    fecha_contratacion = db.Column(db.Date)
    salario = db.Column(db.Float)

    def __init__(self, nombre, edad, especialidad, fecha_contratacion, salario):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        self.fecha_contratacion = fecha_contratacion
        self.salario = salario

    def __repr__(self):
        return f'Enfermero({self.nombre})'

    def __str__(self):
        return f'{self.nombre}'


class Camillero(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    telefono = db.Column(db.String(15))
    fecha_contratacion = db.Column(db.Date)
    activo = db.Column(db.Boolean)

    def __init__(self, nombre, edad, genero, telefono, fecha_contratacion, activo=True):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.telefono = telefono
        self.fecha_contratacion = fecha_contratacion
        self.activo = activo

    def __repr__(self):
        return f'Camillero({self.nombre})'
    
    def __str__(self):
        return f'{self.nombre}'


class Vigilante(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    turno = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __init__(self, nombre, edad, genero, turno):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.turno = turno
    
    def __repr__(self):
        return f'Vigilante({self.nombre})'
    
    def __str__(self):
        return f'{self.nombre} - {self.edad} años'

class Usuario(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    password = db.Column(db.String)
    token = db.Column(db.String)

    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
        self.token = ""

    def __repr__(self):
        return f'Usuario({self.usuario})'
    def __str__(self):
        return f'{self.usuario}'
