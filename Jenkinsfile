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
                    // Instalar virtualenv (no necesitas instalarlo en el entorno global)
                    sh 'python -m pip install --user virtualenv'
                    sh 'python -m virtualenv env'

                    // Editar el archivo env/bin/activate
                    sh 'echo "export FLASK_APP=entrypoint:app" >> env/bin/activate'
                    sh 'echo "export FLASK_ENV=development" >> env/bin/activate'
                    sh 'echo "export APP_SETTINGS_MODULE=config.default" >> env/bin/activate'

                    // Activar el entorno virtual
                    sh 'source env/bin/activate'

                    // Instalar las dependencias de Python desde un archivo requirements.txt
                    sh 'pip install -r requirements.txt'

                    // Guardar las dependencias en un archivo requirements.txt
                    sh 'pip freeze > requirements.txt'
                }
            }
        }

        // ... Otras etapas ...

    }
    post {
        always {
            // Cualquier limpieza que necesites hacer después de la ejecución
            // Por ejemplo, puedes agregar pasos de limpieza aquí, como detener Gunicorn o eliminar archivos temporales
            sh 'pkill -f gunicorn' // Detener Gunicorn si está en ejecución
        }
    }
}
