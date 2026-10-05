pipeline {
    agent any
    stages
    {
        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t kubdemoapp:v1 ."
            }
        }
        stage('Docker Login') {
            steps {
                  bat 'docker login -u mounika2662006 -p Mounika@2006'
                }
            }
        stage('push Docker Image to Docker Hub') {
            steps {
                echo "push Docker Image to Docker Hub"
                bat "docker tag kubdemoapp:v1 mounika2662006/week9:kubeimage1"               
                    
                bat "docker push mounika2662006/week9:kubeimage1"
                
            }
        }
        stage('Deploy to Kubernetes') { 
            steps { 
                    // apply deployment & service 
                    bat 'kubectl apply -f deployment.yaml --validate=false' 
                    bat 'kubectl apply -f service.yaml' 
            } 
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}