pipeline {
    agent any
    options {
        // Timeout counter starts AFTER agent is allocated
        timeout(time: 1, unit: 'SECONDS')
    }
    stages {
        stage('Example') {
            steps {
                git 'https://github.com/Shreyas-Hardy-33/YOLOv11-FLASK_DOCKER_APP.git'
            }
        }
    }
}
