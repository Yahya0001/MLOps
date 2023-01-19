pipeline {
   agent any

   triggers {
        pollSCM "*/5 * * * *"
    }

   stages {

      stage('Build Image') {
         steps {
           sh '''
           docker build -t yahyaallaya/tuto:1.2 .
           '''
         }
      }

      stage('Push Image') {
         steps {
           sh '''
           docker tag yahyaallaya/tuto:1.2  allayayahya/tuto:1.2
           docker login -u allayayahya -p 92492@All
           docker push allayayahya/tuto:1.2
           '''
         }
      }

   }
}