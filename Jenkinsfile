pipeline {
    agent any

    stages {
        stage('Checkout Verification') {
            steps {
                echo 'Repository cloned successfully!'
            }
        }

        stage('List Files') {
            steps {
                bat 'dir'
            }
        }
    }
}
