pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git branch: 'master', credentialsId: 'PROJECT_CREDENTIALS_ID', url: 'PROJECT_GIT_REPO_URL'
            }
        }

        stage('Install dependencies') {
            steps {
                // Install necessary dependencies (Python, Pip, etc.)
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt' // Install project dependencies
            }
        }

        stage('Run tests') {
            steps {
                // Run tests
                sh 'python3 -m pytest'
            }
        }

    }

    post {
        always {
            sh 'echo Tests Completed'
        }
    }
}
