pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'yair0911/shd:1.1'
                }
            }
            steps {
                script {
                    // Agrega tus comandos de Flask aquí
                    sh 'flask db init'
                    sh 'flask db migrate -m "initial_DB"'
                    sh 'flask db upgrade'
                    sh 'flask run --host=0.0.0.0 --port=6001'
                }
            }
        }
    }
}
