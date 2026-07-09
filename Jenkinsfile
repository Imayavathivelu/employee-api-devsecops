pipeline {
    agent any

    environment {
        IMAGE_NAME = "imayavathi/employee-api:v1"
        PYTHON = "C:\\Users\\imaya\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
         TRIVY ="C:\\Users\\imaya\\AppData\\Local\\Microsoft\\WinGet\\Links\\trivy.exe"

    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Tools') {
            steps {
                bat '"%PYTHON%" --version'
                bat 'docker --version'
                bat 'kubectl version --client'
            }
        }

        stage('Install Dependencies') {
            steps {
               bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('SAST - SonarQube') {
            steps {
                echo 'Running SonarQube Analysis...'
            }
        }

       stage('SCA - pip-audit') {
    steps {
        catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
            bat '"%PYTHON%" -m pip install pip-audit'
            bat '"%PYTHON%" -m pip_audit'
        }
    }
}

        stage('Docker Build') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Trivy Scan') {
    steps {
        bat '"%TRIVY%" image %IMAGE_NAME%'
    }
}

        stage('Docker Push') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
        )]) {
            bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
            bat 'docker push %IMAGE_NAME%'
        }
    }
}

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get svc'
            }
        }
    }
}
