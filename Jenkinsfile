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
                    // Instalar virtualenv localmente en el directorio del proyecto
                    sh "python -m pip install --target . virtualenv"

                    // Verificar si el directorio 'env' ya existe
                    if (!fileExists('env')) {
                        // Crear un entorno virtual en el directorio del proyecto si no existe
                        sh "python -m virtualenv env"
                    }

                    // Activar el entorno virtual
                    sh "source env/bin/activate"

                    // Instalar Flask en el entorno virtual
                    sh "pip install Flask"

                    // Editar el archivo env/bin/activate (si es necesario)
                    sh "echo 'export FLASK_APP=entrypoint:app' >> env/bin/activate"
                    sh "echo 'export FLASK_ENV=development' >> env/bin/activate"
                    sh "echo 'export APP_SETTINGS_MODULE=config.default' >> env/bin/activate"

                    // Instalar las dependencias de Python desde un archivo requirements.txt
                    sh "pip install --target . -r requirements.txt"

                    // Guardar las dependencias en un archivo requirements.txt
                    sh "pip freeze > requirements.txt"
                }
            }
        }
        stage('Initialization and Execution') {
            steps {
                // Activar el entorno virtual
                sh "source env/bin/activate"
                sh "env/bin/flask db init"
                sh "env/bin/flask db migrate -m 'Initial_DB'"
                sh "env/bin/flask db upgrade"
            }
        }
        stage('Deployment') {
            steps {
                // Activar el entorno virtual
                sh "source env/bin/activate"
                sh "flask run &"
                script {
                    retry(20) {
                        def response = sh(script: "curl -s -o /dev/null -w '%{http_code}' http://localhost:5000", returnStatus: true)
                        return response == 200
                    }
                }
            }
        }
    }
    post {
        always {
            // Detener Flask usando pkill
            sh "pkill -f 'flask run'"
        }
    }
}
