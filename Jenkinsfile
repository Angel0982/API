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

                    // Crear un entorno virtual en el directorio del proyecto
                    sh "python -m virtualenv env"

                    // Editar el archivo env/bin/activate (si es necesario)
                    sh "echo 'export FLASK_APP=entrypoint:app' >> env/bin/activate"
                    sh "echo 'export DEBUG=1' >> env/bin/activate"
                    sh "echo 'export APP_SETTINGS_MODULE=config.default' >> env/bin/activate"
                    sh "cat env/bin/activate"

                    // Activar el entorno virtual y ejecutar comandos
                    sh "chmod +x env/bin/activate"
                    sh "./env/bin/activate && pip install --target . -r requirements.txt"
                    sh "./env/bin/activate && pip freeze > requirements.txt"
                }
            }
        }
        stage('Initialization and Execution') {
            steps {
                // Activar el entorno virtual y ejecutar comandos de Flask
                sh "./env/bin/activate && flask db init"
                sh "./env/bin/activate && flask db migrate -m 'Initial_DB'"
                sh "./env/bin/activate && flask db upgrade"
            }
        }
        stage('Deployment') {
            steps {
                // Activar el entorno virtual antes de ejecutar el servidor Flask
                sh "./env/bin/activate && flask run &"
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
            sh "pkill -f 'flask run'"
        }
    }
}
