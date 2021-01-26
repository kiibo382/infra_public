terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
  profile = "ccti-dev"
  region  = "ap-northeast-1"
}

resource "aws_instance" "example" {
  ami           = "ami-01748a72bed07727c"
  instance_type = "t2.micro"
}
