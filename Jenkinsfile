
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'v1',
                    url: 'https://github.com/VR-Sindhujha/online-exam.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        
stage('Build Docker Image') {
    steps {
        bat '"C:\\Users\\ADMIN\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" --version'
        bat '"C:\\Users\\ADMIN\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t sindhujha06/online-exam:v1 .'
    }
}

    }
}
