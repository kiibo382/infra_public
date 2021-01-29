variable "profile" {}
variable "region" {}

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

resource "aws_s3_bucket" "lambda-code-bucket" {
  bucket = "kizawa-lambda-code-bucket"
  acl    = "private"
}
