# Usa una imagen de Python 3.7 como base
FROM python:3.7-bullseye

# Cambia al usuario root para realizar las acciones de instalación
USER root

# Instala las herramientas necesarias
RUN pip install virtualenv

# Crea un directorio de trabajo
WORKDIR /app

# Configuración y configuración del entorno virtual
RUN virtualenv env
RUN /bin/bash -c "source env/bin/activate && \
    pip install flask sqlalchemy marshmallow flask_restful flask_sqlalchemy flask_migrate flask_marshmallow marshmallow_sqlalchemy && \
    pip freeze > requirements.txt && \
    echo 'export FLASK_APP=entrypoint:app' >> env/bin/activate && \
    echo 'export FLASK_ENV=development' >> env/bin/activate && \
    echo 'export APP_SETTINGS_MODULE=config.default' >> env/bin/activate"

# Copia los archivos de tu aplicación al directorio de trabajo en el contenedor
COPY . .

# Inicialización y ejecución de la aplicación Flask
CMD /bin/bash -c "source env/bin/activate && \
    flask db init && \
    flask db migrate -m 'Initial_DB' && \
    flask db upgrade && \
    flask run --host=0.0.0.0
