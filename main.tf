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

resource "aws_s3_bucket" "s3-call-recording-bucket" {
  bucket = "kizawa-call-recording-bucket"
  acl    = "private"
}

resource "aws_s3_bucket" "s3-transcribe-bucket" {
  bucket = "kizawa-transcribe-bucket"
  acl    = "private"
}

resource "aws_s3_bucket" "s3-comprehend-bucket" {
  bucket = "kizawa-comprehend-bucket"
  acl    = "private"
}
