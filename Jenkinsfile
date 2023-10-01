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
            steps {
                script {
                    // Instalar virtualenv localmente en el directorio del proyecto
                    sh "python -m pip install --target . virtualenv"

                    // Crear un entorno virtual en el directorio del proyecto
                    sh "python -m virtualenv env"

                    // Activar el entorno virtual y ejecutar comandos
                    sh "env/bin/python -m pip install --target . -r requirements.txt"
                    sh "env/bin/python entrypoint.py db init"
                    sh "env/bin/python entrypoint.py db migrate -m 'Initial_DB'"
                    sh "env/bin/python entrypoint.py db upgrade"
                }
            }
        }
        stage('Deployment') {
            steps {
                // Activar el entorno virtual antes de ejecutar el servidor Flask
                sh "env/bin/python entrypoint.py run"
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
            sh "pkill -f 'python entrypoint.py run'"
        }
    }
}
