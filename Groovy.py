pipeline {
    agent any  // <-- REQUIRED: Tells Jenkins to run this on any available executor

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Virtualenv') {
            steps {
                // Windows build nodes (cmd/bat)
                bat '''
                    if not exist venv (
                        python -m venv venv
                    )
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest Automation') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest -vs --html=report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])
        }
    }
}