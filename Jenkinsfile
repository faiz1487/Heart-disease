pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = "faizan141/heart-disease"   // Your Docker Hub Repo
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/faiz1487/Heart-disease.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKERHUB_REPO:$IMAGE_TAG .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withDockerRegistry(credentialsId: 'dockerhub-credentials', url: 'https://index.docker.io/v1/') {
                    // Successfully authenticated
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                withDockerRegistry(credentialsId: 'dockerhub-credentials', url: 'https://index.docker.io/v1/') {
                    sh 'docker push $DOCKERHUB_REPO:$IMAGE_TAG'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f heart-app || true
                docker run -d -p 5000:5000 --name heart-app $DOCKERHUB_REPO:$IMAGE_TAG
                '''
            }
        }
    }
}
