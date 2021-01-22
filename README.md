# Fursa Final Project ( Currency converter )
###### About 
Calculate live currency and foreign exchange rates with this free currency converter. You can convert currencies and precious metals with this currency calculator.

* ## Usage 
    *   access the main-page of the website : http://server-ip:81/
        ![GitHub Logo](/ScreenShots/homepage.png)

    *   access the log-page  : http://server-ip:81/log
        ![GitHub Logo](/ScreenShots/log.png)
    
* ## How to Run 
    1. **via Terraform (Run on AWS)**
        `Terraform apply -auto-approve`
         using this command will start an  EC2 instanse and run all system (Currency converter )
         you can access the website using the ip of the ec2 and the port 81 
        
        `Terraform destroy -auto-approve` 
        will remove and clean everything 

    2. **via Docker** 
        `sudo docker-compose -f docker-compose.yaml up `
        
        using this command will start 3 containers : 
        1. mysql 
        2. backend
        3. frontend 
        
        you access the system using this link : http://localhost:81/

    3. **via Kubernetes (k8s)**
        `kubelet apply -f ./k8s` 
        1. backend-deployment.yaml 
        2. frontend-deployment.yaml 
        3. mysql-deployment.yaml

    4. **Jenkins**
    Pipeline 
        `
        pipeline {
        agent any
            stages {
                stage('Build') {
                    steps {
                        sh 'git clone https://github.com/shadifadila2018/fursa_final_project.git || exit 0'
                        sh 'sudo docker-compose -f ./fursa_final_project/docker-compose.yaml up'
                        }
                }
            }
        }
        `
    



