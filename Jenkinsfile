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
                    // Configura un directorio de caché personalizado para pip
                    sh "export XDG_CACHE_HOME=/home/yair/API/cache"

                    // Instalar virtualenv localmente en el directorio del proyecto
                    sh "python -m pip install --target . virtualenv"

                    // Crear un entorno virtual en el directorio del proyecto
                    sh "python -m virtualenv env"

                    // Activar el entorno virtual con el operador punto
                    sh ". env/bin/activate"

                    // Editar el archivo env/bin/activate (si es necesario)
                    sh "echo 'export FLASK_APP=entrypoint:app' >> env/bin/activate"
                    sh "echo 'export FLASK_ENV=development' >> env/bin/activate"
                    sh "echo 'export APP_SETTINGS_MODULE=config.default' >> env/bin/activate"

                    // Instalar las dependencias de Python desde un archivo requirements.txt
                    sh "pip install -r requirements.txt"

                    // Guardar las dependencias en un archivo requirements.txt
                    sh "pip freeze > requirements.txt"
                }
            }
        }

        // Resto de las etapas (Initialization and Execution, Deployment) sin cambios
    }
    post {
        always {
            // Cualquier limpieza que necesites hacer después de la ejecución
            // Por ejemplo, puedes agregar pasos de limpieza aquí, como detener Gunicorn o eliminar archivos temporales
            script {
                try {
                    // Detener Gunicorn si está en ejecución
                    sh 'pkill -f gunicorn'
                } catch (Exception e) {
                    echo 'Gunicorn no estaba en ejecución.'
                }
            }
        }
    }
}
