terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
  profile = var.profile
  region  = var.region
}

resource "aws_instance" "example" {
  ami           = "ami-01748a72bed07727c"
  instance_type = "t2.micro"
}
