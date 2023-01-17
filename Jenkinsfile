pipeline {
   agent any

   triggers {
        pollSCM "*/5 * * * *"
    }

   stages {
      stage('Prepare Envirement') {
         steps {
            sh '''
            pip install -r requirements.txt
            '''
         }
      }

      stage('Build Docker Image') {
         steps {
           sh '''
           docker build -t yahyaallaya/tuto:0.1 .
           '''
         }
      }

      stage('Push Docker Image') {
         steps {
           sh '''
           docker tag yahyaallaya/tuto:0.1  allayayahya/tuto:0.1
           docker login -u allayayahya -p 92492@All
           docker push allayayahya/tuto:0.1
           '''
         }
      }

      stage('Deploy to kubernetes') {
         steps {
           sh '''
           minikube start --driver=docker
           kubectl apply -f kubernetes.yaml
           '''
         }
      }

      

   }
}