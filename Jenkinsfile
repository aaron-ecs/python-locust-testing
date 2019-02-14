node {
    stage('Build & Test') {
        checkout scm
        sh "docker build . -t aaronmwilliams/python-locust-testing"
        sh "docker-compose up --exit-code-from tests"
    }
}