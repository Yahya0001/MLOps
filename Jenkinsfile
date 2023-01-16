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
           docker build -t yahyaallaya/tuto:latest .
           '''
         }
      }

      stage('Push Docker Image') {
         steps {
           sh '''
           docker tag yahyaallaya/tuto:latest  allayayahya/tuto:latest
           docker login -u allayayahya -p 92492@All
           docker push allayayahya/tuto:latest
           '''
         }
      }

      stage('Deploy to kubernetes') {
         steps {
           sh '''
           kubectl apply -f kubernetes.yaml
           '''
         }
      }

      

   }
}