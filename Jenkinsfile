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
                    // Crear un directorio para el entorno virtual y paquetes de usuario
                    sh 'mkdir -p ~/.local'

                    // Instalar virtualenv en el directorio de usuario
                    sh 'python -m pip install --user virtualenv'

                    // Crear un entorno virtual en un directorio personal
                    sh 'python -m virtualenv ~/.local/env'

                    // Editar el archivo env/bin/activate
                    sh 'echo "export FLASK_APP=entrypoint:app" >> ~/.local/env/bin/activate'
                    sh 'echo "export FLASK_ENV=development" >> ~/.local/env/bin/activate'
                    sh 'echo "export APP_SETTINGS_MODULE=config.default" >> ~/.local/env/bin/activate'

                    // Activar el entorno virtual
                    sh 'source ~/.local/env/bin/activate'

                    // Instalar las dependencias de Python desde un archivo requirements.txt
                    sh 'pip install -r requirements.txt'

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
                    // Instalar Gunicorn para servir la aplicación Flask (dentro del entorno virtual)
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
