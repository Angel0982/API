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
                    sh "pip install --target . -r requirements.txt"

                    // Guardar las dependencias en un archivo requirements.txt
                    sh "pip freeze > requirements.txt"

                    // Instalar Flask localmente en el directorio del proyecto (si no está instalado)
                    sh "pip install --target env Flask"
                }
            }
        }
        stage('Initialization and Execution') {
            steps {
                script {
                    // Activar el entorno virtual antes de continuar
                    sh ". env/bin/activate"

                    // Inicializar la base de datos (flask db init)
                    sh "flask db init"

                    // Crear una migración de la base de datos (flask db migrate)
                    sh "flask db migrate -m 'Initial_DB'"

                    // Aplicar la migración a la base de datos (flask db upgrade)
                    sh "flask db upgrade"

                    // Ejecutar la aplicación Flask (flask run)
                    sh "flask run &"
                }
            }
        }
    }
    post {
        always {
            // Cualquier limpieza que necesites hacer después de la ejecución
            // Por ejemplo, puedes agregar pasos de limpieza aquí, como detener Gunicorn o eliminar archivos temporales
            script {
                try {
                    // Detener Gunicorn usando kill
                    sh 'pkill -f gunicorn'
                } catch (Exception e) {
                    echo 'Gunicorn no estaba en ejecución.'
                }
            }
        }
    }
}
