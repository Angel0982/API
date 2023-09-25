pipeline {
    agent {
        docker {
            image 'python:3.7-bullseye'
        }
    }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                // Aquí puedes agregar cualquier paso necesario para construir tu aplicación
            }
        }
        stage('Configure') {
            steps {
                script {
                    // Instalar virtualenv
                    sh 'pip install virtualenv'

                    // Crear un entorno virtual
                    sh 'virtualenv env'

                    // Editar el archivo env/bin/activate
                    sh 'echo "export FLASK_APP=entrypoint:app" >> env/bin/activate'
                    sh 'echo "export FLASK_ENV=development" >> env/bin/activate'
                    sh 'echo "export APP_SETTINGS_MODULE=config.default" >> env/bin/activate'

                    // Activar el entorno virtual
                    sh 'source env/bin/activate'

                    // Instalar las dependencias de Python desde un archivo requirements.txt
                    sh 'pip install -r requirements.txt'
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

                    // Ejecutar la aplicación Flask (debes ejecutarlo en segundo plano)
                    sh 'nohup flask run &'
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
