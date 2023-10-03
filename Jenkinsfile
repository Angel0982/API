pipeline {
    agent any

    stages {
        stage('Run Docker Container') {
            steps {
                script {
                    // Ejecutar la imagen Docker
                    def dockerImage = docker.image('88786ce4e4f6')
                    def container = dockerImage.run('-p 6001:6001', 'bash', '-c', 'source env/bin/activate && flask db init && flask db migrate -m "initial_DB" && flask db upgrade && flask run --host=0.0.0.0 --port=6001')
                    container.inside {
                        // Los comandos se ejecutarán dentro del contenedor Docker
                        sh '''
                            source env/bin/activate
                            flask db init
                            flask db migrate -m "initial_DB"
                            flask db upgrade
                            flask run --host=0.0.0.0 --port=6001
                        '''
                    }
                }
            }
        }
    }
}
