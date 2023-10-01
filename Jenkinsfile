pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build and Setup') {
            steps {
                // Construir la imagen Docker con el Dockerfile modificado
                script {
                    dockerImage = docker.build('jenkins-docker', '-f Dockerfile .')
                }
                // Realizar acciones de configuración en la imagen Docker
                sh '''
                    docker run --rm -d -p 0.0.0.0:5000:5000 -v $PWD:/app -w /app jenkins-docker /bin/bash -c "
                    source env/bin/activate &&
                    flask db init &&
                    flask db migrate -m 'Initial_DB' &&
                    flask db upgrade &&
                    flask run --host=0.0.0.0"
                '''
            }
        }
        stage('Wait for Flask to Start') {
            steps {
                script {
                    def isFlaskRunning = false
                    def maxAttempts = 30
                    def attempt = 0
                    def apiUrl = 'http://0.0.0.0:5000'  // La URL de tu API Flask

                    // Esperar hasta que la API Flask esté en funcionamiento o hasta que se alcance el número máximo de intentos
                    while (!isFlaskRunning && attempt < maxAttempts) {
                        try {
                            // Realizar una solicitud HTTP a la API Flask
                            def response = httpRequest(url: apiUrl, validResponseCodes: '200', ignoreSslErrors: true)
                            if (response.status == 200) {
                                isFlaskRunning = true
                            }
                        } catch (Exception e) {
                            // La solicitud falló, esperar unos segundos antes de intentar nuevamente
                            sleep time: 10, unit: 'SECONDS'
                            attempt++
                        }
                    }

                    if (isFlaskRunning) {
                        echo "La API Flask está en funcionamiento. Puedes acceder a ella en: $apiUrl"
                    } else {
                        error "La API Flask no se pudo iniciar después de $maxAttempts intentos."
                    }
                }
            }
        }
    }
}
