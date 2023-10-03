pipeline {
    agent none

    stages {
        stage('Run Docker Container') {
            steps {
                script {
                    // Ejecutar el contenedor Docker
                    def container = docker.image('88786ce4e4f6').run('-p 6001:6001', 'bash', '-c', 'source env/bin/activate && flask db init && flask db migrate -m "initial_DB" && flask db upgrade && flask run --host=0.0.0.0 --port=6001')
                    // Esperar a que el contenedor termine y obtener el código de salida
                    def exitCode = container.waitForStatus('EXITED')
                    // Mostrar el código de salida
                    echo "Código de salida del contenedor: $exitCode"
                }
            }
        }
    }
}
