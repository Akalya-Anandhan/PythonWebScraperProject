pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Scraper') {
            steps {
                bat 'python app\\scraper.py'
            }
        }
    }
}
