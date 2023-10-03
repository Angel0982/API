pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clona el repositorio de código fuente
                checkout scm
            }
        }
        
        stage('Build and Run Docker Container') {
            steps {
                script {
                    // Ejecuta el contenedor Docker con la imagen ID 88786
                    sh 'docker run -d 88786'
                }
            }
        }
    }
}
