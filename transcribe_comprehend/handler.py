from __future__ import print_function
import boto3
import datetime
import os
import urllib.parse


s3 = boto3.client("s3")
transcribe = boto3.client("transcribe")


def lambda_handler(event, context):
    bucket = event["pathParameters"]["bucketname"]
    key = event["pathParameters"]["key"]
    
