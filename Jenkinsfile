pipeline {
    agent any
    
    stages {
        stage('Configuración') {
            steps {
                sh 'pip install virtualenv env'
                sh 'virtualenv env'
                sh 'echo "export FLASK_APP=\"entrypoint:app\"" >> env/bin/activate'
                sh 'echo "export FLASK_ENV=\"development\"" >> env/bin/activate'
                sh 'echo "export APP_SETTINGS_MODULE=\"config.default\"" >> env/bin/activate'
                sh 'source env/bin/activate'
                sh 'pip install flask sqlalchemy marshmallow flask_restful flask_sqlalchemy flask_migrate flask_marshmallow marshmallow_sqlalchemy'
                sh 'pip freeze > requirements.txt'
            }
        }
        
        stage('Inicialización y Ejecución') {
            steps {
                sh 'source env/bin/activate'
                sh 'flask db init'
                sh 'flask db migrate -m "Initial_DB"'
                sh 'flask db upgrade'
                sh 'flask run'
            }
        }
    }
}
