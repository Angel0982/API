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
                    dockerImage = docker.build('my-flask-app', '-f Dockerfile .')
                }
                // Realizar acciones de configuración en la imagen Docker
                sh '''
                    docker run --rm -d -p 5000:5000 -v /var/jenkins_home/workspace/API:/app -w /app my-flask-app /bin/bash -c "source env/bin/activate && flask db init && flask db migrate -m 'Initial_DB' && flask db upgrade && flask run --host=0.0.0.0"
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
                    // Esperar a que Flask esté en funcionamiento antes de continuar
                    timeout(time: 5, unit: 'MINUTES') {
                        // Puedes agregar una lógica para verificar si Flask está listo para recibir solicitudes
                        // Por ejemplo, puedes realizar una solicitud HTTP de prueba a la API para verificar su disponibilidad
                        // Cuando Flask esté listo, proporciona la URL de la API al usuario
                        input(message: 'La API Flask está en funcionamiento. Puedes acceder a ella en:', parameters: [string(defaultValue: 'http://192.168.3.164:5000', description: 'URL de la API', name: 'API_URL')])
                    }
                }
            }
        }
    }
}
