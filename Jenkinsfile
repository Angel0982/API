pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7-bullseye'
                }
            }
            steps {
                script {
                    // Instalar virtualenv
                    sudo -H sh 'pip install virtualenv env'

                    // Crear un entorno virtual
                    sudo -H sh 'virtualenv env'

                    // Editar el archivo env/bin/activate
                    sh 'echo "export FLASK_APP=entrypoint:app" >> env/bin/activate'
                    sh 'echo "export FLASK_ENV=development" >> env/bin/activate'
                    sh 'echo "export APP_SETTINGS_MODULE=config.default" >> env/bin/activate'

                    // Activar el entorno virtual
                    sh 'source env/bin/activate'

                    // Instalar las dependencias de Python
                    sh 'pip install flask sqlalchemy marshmallow flask_restful flask_sqlalchemy flask_migrate flask_marshmallow marshmallow_sqlalchemy'

                    // Guardar las dependencias en un archivo requirements.txt
                    sh 'pip freeze > requirements.txt'
                }
            }
        }

        stage('Initialization and Execution') {
            steps {
                script {
                    // Inicializar la base de datos
                    sh 'flask db init'

                    // Crear una migración inicial
                    sh 'flask db migrate -m "Initial_DB"'

                    // Aplicar la migración a la base de datos
                    sh 'flask db upgrade'

                    // No ejecutar 'flask run' aquí, lo haremos en la etapa de implementación
                }
            }
        }

        stage('Deployment') {
            agent any
            steps {
                script {
                    // Instalar Gunicorn para servir la aplicación Flask
                    sh 'pip install gunicorn'

                    // Ejecutar la aplicación Flask usando Gunicorn
                    sh 'gunicorn -b 0.0.0.0:8000 entrypoint:app &'
                }
            }
        }
    }
    post {
        always {
            // Cualquier limpieza que necesites hacer después de la ejecución
            // Por ejemplo, puedes agregar pasos de limpieza aquí, como detener Gunicorn o eliminar archivos temporales
            sh 'pkill -f gunicorn' // Detener Gunicorn si está en ejecución
        }
    }
}
