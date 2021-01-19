# Configure the AWS Provider
provider "aws"  {
    region = "us-east-1"
    access_key = "AKIAT56U5USABOFZOYF2"
    secret_key = "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"
}


resource "aws_instance" "web" {
  ami           = "ami-0885b1f6bd170450c"
  instance_type = "t2.xlarge"
  key_name          = "mykey"
  user_data = <<-EOF
                #!/bin/bash
                wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
                sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
                    /etc/apt/sources.list.d/jenkins.list'
                sudo apt update -y
                sudo apt install openjdk-11-jdk -y
                sudo apt-get install jenkins -y
                EOF
  tags = {
    Name = "jenkins"
  }
}

output "ec2-ip" {
  value = aws_instance.web.public_ip
}


