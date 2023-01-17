pipeline {
   agent any

   triggers {
        pollSCM "*/5 * * * *"
    }

   stages {

      stage('Build Image') {
         steps {
           sh '''
           docker build -t yahyaallaya/tuto:latest .
           '''
         }
      }

      stage('Push Image') {
         steps {
           sh '''
           docker tag yahyaallaya/tuto:latest  allayayahya/tuto:latest
           docke login -u allayayahya -p 92492@All
           docker push allayayahya/tuto:latest
           '''
         }
      }

   }
}