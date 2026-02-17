// pipeline {
//     agent any

//     environment {
//         IMAGE_NAME = "scientific-calculator"
//         CONTAINER_NAME = "scientific-calculator-container"
//     }

//     stages {

//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t $IMAGE_NAME .'
//             }
//         }

//         stage('Stop Old Container') {
//             steps {
//                 sh 'docker stop $CONTAINER_NAME || true'
//                 sh 'docker rm $CONTAINER_NAME || true'
//             }
//         }

//         stage('Run New Container') {
//             steps {
//                 sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME'
//             }
//         }
//     }
// }
pipeline {
    agent any

    environment {
        IMAGE_NAME = "scientific-calculator"
        CONTAINER_NAME = "calculator-container"
    }

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh "docker stop $CONTAINER_NAME || true"
                    sh "docker rm $CONTAINER_NAME || true"
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME"
                }
            }
        }
    }
}
