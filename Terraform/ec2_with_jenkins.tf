# Configure the AWS Provider
provider "aws"  {
    region = "us-east-1"
    access_key = "access_key"
    secret_key = "secret_key"
}

resource "aws_instance" "web" {
  ami           = "ami-0885b1f6bd170450c"
  instance_type = "t2.large"
  key_name          = "mykey"
  user_data = <<-EOF
                #!/bin/bash
                wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
                sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
                    /etc/apt/sources.list.d/jenkins.list'
                sudo apt update -y
                sudo apt install openjdk-11-jdk -y
                sudo apt-get install jenkins -y
                sudo apt-get install docker.io -y
                sudo -i
                echo -e "jenkins ALL= NOPASSWD: ALL" >> /etc/sudoers
                sudo docker login -u shadifadila -p 0538241788@@

                sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
                sudo chmod +x /usr/local/bin/docker-compose
                
                git clone https://github.com/shadifadila2018/fursa_final_project
                sudo docker-compose -f ./fursa_final_project/docker-compose.yaml up

                EOF
  tags = {
    Name = "jenkins"
  }
}

output "ec2-ip" {
  value = aws_instance.web.public_ip
}


