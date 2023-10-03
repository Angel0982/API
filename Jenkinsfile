pipeline {
    agent {
        docker {
            image '88786ce4e4f6'
            args '-u root:root' // Opcional: Cambiar el usuario y grupo de Docker si es necesario
        }
    }
    stages {
        stage('Build and Run') {
            steps {
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
