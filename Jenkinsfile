pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = "faiz18887/heart-disease"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/faiz1487/Heart-disease.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKERHUB_REPO}:${IMAGE_TAG}")
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                withDockerRegistry(credentialsId: 'docker', url: 'https://index.docker.io/v1/') {
                    echo "Logged in to DockerHub"
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                script {
                    dockerImage.push("${IMAGE_TAG}")
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                  docker rm -f heart-disease-app || true
                  docker run -d -p 5000:5000 --name heart-disease-app ${DOCKERHUB_REPO}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
