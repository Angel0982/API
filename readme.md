Código del API de la materia de Automatización de Infraestructura Digital 1.
master:    MICHEL OROZCO CARRERA
branches:
>valeria:  CONTRERAS ZARAGOZA VALERIA
>oscar:    DOMINGUEZ GARCIA OSCAR
>miguel:   FLORES NESTLE MIGUEL ANGEL
>marlen:   FRUCTUOSO BRAVO MARLEN
>karen:    FUENTES ARCOS KAREN JULIE
>denilson: PEREZ EUGENIO DENILSON ISAAC
>janeth:   RIVERA HERNANDEZ JANETH
>angel:    SANCHEZ ORTEGA ANGEL YAIR

=== LIBRERÍAS ===

Flask
SQLAlchemy
Marshmallow
---
Flask_Restful
Flask_SQLAlchemy
Flask_Migrate
Flask_Marshmallow
Marshmallow_SQLAlchemy

=== ESTRUCTURA DE ARCHIVOS/CARPETAS ===

+api-peliculas
|_+ app
  |_+ common
    |_ __init__.py
    |_ error_handling.py   # Utilidades para el manejo de errores
  |_+ films
    |_+ api_v1_0
      |_ __init__.py
      |_ resources.py   # Endpoints del API
      |_ schemas.py     # Esquemas para serializar los modelos
    |_ __init__.py
    |_ models.py   # Modelos
  |_ __init__.py   # Configuración de la aplicación
  |_ db.py         # Configuración de la base de datos
  |_ ext.py        # Instanciación de las extensiones
|_+ config         # Directorio para la configuración
  |_ __init__.py
  |_ default.py    # Configuración por defecto
|_ entrypoint.py   # Crea la instancia de la app

==> Estructura de base de datos:

humedad:
> id, clave primaria
> valor, humedad porcetual
> timestamp, fecha y hora de la lectura
> usuario, usuario que registra el valor
> status, valor A (activo) ó I (inactivo)
temperatura:
> id, clave primaria
> valor, temperatura en grados celsius
> timestamp, fecha y hora de la lectura
> usuario, usuario que registra el valor
> status, valor A (activo) ó I (inactivo)
luminosidad:
> id, clave primaria
> valor, luxes
> timestamp, fecha y hora de la lectura
> usuario, usuario que registra el valor
> status, valor A (activo) ó I (inactivo)
movimiento:
> id, clave primaria
> timestamp, fecha y hora de la lectura
> usuario, usuario que registra el valor
> status, valor A (activo) ó I (inactivo)
distancia:
> id, clave primaria
> valor, centimetros desde el sensor
> timestamp, fecha y hora de la lectura
> usuario, usuario que registra el valor
> status, valor A (activo) ó I (inactivo)

usuario:
> id, clave primaria
> usuario, nombre de usuario de ingreso
> password, la clave de ingreso del usuario
> token, la cadena de indentificación del usuario
> status, valor A (activo) ó I (inactivo)

==> Se cambia a:

Paciente:
> id = db.Column(db.Integer, primary_key=True)
> nombre = db.Column(db.String(100), nullable=False)
> edad = db.Column(db.Integer, nullable=False)
> genero = db.Column(db.String(10), nullable=False)
> direccion = db.Column(db.String(200))
> fecha_ingreso = db.Column(db.DateTime, default=datetime.datetime.utcnow)
> estado = db.Column(db.String(20), default='En tratamiento')
> usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

Doctor:
> id = db.Column(db.Integer, primary_key=True)
> name = db.Column(db.String(100), nullable=False)
> specialization = db.Column(db.String(100))
> contact_number = db.Column(db.String(15))
> email = db.Column(db.String(100))

Enfermero:
> id = db.Column(db.Integer, primary_key=True)
> nombre = db.Column(db.String(50), nullable=False)
> edad = db.Column(db.Integer)
> especialidad = db.Column(db.String(100))
> fecha_contratacion = db.Column(db.Date)
> salario = db.Column(db.Float)

Camillero:
> id = db.Column(db.Integer, primary_key=True)
> nombre = db.Column(db.String(50))
> edad = db.Column(db.Integer)
> genero = db.Column(db.String(10))
> telefono = db.Column(db.String(15))
> fecha_contratacion = db.Column(db.Date)
> activo = db.Column(db.Boolean)

Vigilante:
> id = db.Column(db.Integer, primary_key=True)
> nombre = db.Column(db.String(100), nullable=False)
> edad = db.Column(db.Integer)
> genero = db.Column(db.String(10))
> turno = db.Column(db.String(20))
> timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

Usuario:
> id = db.Column(db.Integer, primary_key=True)
> usuario = db.Column(db.String)
> password = db.Column(db.String)
> token = db.Column(db.String)

=== env/bin/activate ===

...
export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"

=== proceso de configuración ===

1. pip install virtualenv env
2. virtualenv env
3. editar: env/bin/activate
...
export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"
4. source env/bin/activate
5. pip install flask sqlalchemy marshmallow flask_restful flask_sqlalchemy flask_migrate flask_marshmallow marshmallow_sqlalchemy
6. pip freeze > requirements.txt

=== proceso de inicialización y ejecución ===

1. flask db init
2. flask db migrate -m "Initial_DB"
3. flask db upgrade
*. flask run
