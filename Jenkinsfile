pipeline {
    agent any

    environment {
        IMAGE_NAME = "scientific-calculator"
        CONTAINER_NAME = "scientific-calculator-container"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ksathvikreddy31/calculator.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }
}