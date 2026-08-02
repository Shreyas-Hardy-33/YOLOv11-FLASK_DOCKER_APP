pipeline {
    agent any
    stages {
        stage('clone') {
            steps {
                git 'https://github.com/Shreyas-Hardy-33/YOLOv11-FLASK_DOCKER_APP.git'
            }
        }

        stage('Build Docker Image'){
            steps{
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }
        
    }
}
