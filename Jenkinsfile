
pipeline {
    agent {
        label 'agent'
    }

    environment {
        DOCKER_IMAGE_NAME = "flask-api"
        DOCKER_IMAGE_TAG = "v1"
        CONTAINER_NAME = "flask-api-docker"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Puxando o código do GitHub...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building the image ${env.DOCKER_IMAGE_NAME}:${env.DOCKER_IMAGE_TAG}..."
                bat "docker build -t ${env.DOCKER_IMAGE_NAME}:${env.DOCKER_IMAGE_TAG} ."
            }
        }

        stage('Stop and Remove Old Container') {
            steps {
                echo "Stops and removes the old container if exists"

                bat "docker stop ${env.CONTAINER_NAME} || exit 0"
                bat "docker rm ${env.CONTAINER_NAME} || exit 0"
            }
        }

        stage('Run New Container') {
            steps {
                echo "Run our container"
                bat "docker run -d --name ${env.CONTAINER_NAME} -p 5000:5000 ${env.DOCKER_IMAGE_NAME}:${env.DOCKER_IMAGE_TAG}"
            }
        }
    }

    post {
        always {
            echo 'Limpando imagens Docker antigas...'
            bat 'docker image prune -f'
        }
        success {
            bat 'echo Pipeline executed successfully'
        }
        failure {
            echo 'The pipeline failed'
        }
    }
}