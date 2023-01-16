pipeline {
   agent any

   triggers {
        pollSCM "*/5 * * * *"
    }

   stages {
      stage('Preparation') {
         steps {
            echo "hi"
         }
      }
      stage('Build') {
         steps {
            sh '''
            pip install -r requirements.txt
            '''
         }
      }

      stage('Build Image') {
         steps {
           sh '''
           docker build -t yahyaallaya/MLOps:latest .
           '''
         }
      }

      stage('Push Image') {
         steps {
           sh '''
           docker tag yahyaallaya/MLOps:latest  allayayahya/MLOps:latest
           docker login -u allayayahya -p 92492@All
           docker push allayayahya/MLOps:latest
           '''
         }
      }

   }
}