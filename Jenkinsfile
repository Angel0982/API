pipeline {
    agent none
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
        }
        stage('Configure') {
            steps {
                script {
                    // Instalar virtualenv
                    sh 'pip install virtualenv env'

                    // Crear un entorno virtual
                    sh 'virtualenv env'

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

                    // Ejecutar la aplicación Flask
                    sh 'flask run'
                }
            }
        }
    }
    post {
        always {
            // Cualquier limpieza que necesites hacer después de la ejecución
        }
    }
}
