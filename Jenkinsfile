pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Construir la imagen Docker
                    docker.build('mi_aplicacion_flask')
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Ejecutar el contenedor Docker
                    docker.image('mi_aplicacion_flask').run('-p 6001:6001', '--name mi_aplicacion_flask_container', 'bash', '-c', 'source env/bin/activate && flask db init && flask db migrate -m "initial_DB" && flask db upgrade && flask run --host=0.0.0.0 --port=6001')
                }
            }
        }
    }

    post {
        always {
            // Detener y eliminar el contenedor después de finalizar
            script {
                docker.image('mi_aplicacion_flask').stop()
                docker.image('mi_aplicacion_flask').remove(force: true)
            }
        }
    }
}
