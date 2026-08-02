pipeline {
    agent any
    stages {
        stage('clone') {
            steps {
                git 'https://github.com/Shreyas-Hardy-33/YOLOv11-FLASK_DOCKER_APP.git'
            }
        }

        stage('Install dependencies'){
            steps{
                bash 'pip install -r requirements.txt'
            }
        }
        
    }
}
