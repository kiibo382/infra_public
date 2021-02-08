import boto3
import datetime
import os
import urllib.parse
import json
import base64


def get(event, context):
    s3 = boto3.client("s3")
    records_bucket = event["queryStringParameters"]["records_bucket"]
    file_name = event["queryStringParameters"]["file_name"]

    try:
        # imageBody = base64.b64decode(event["body-json"])
        response_body = s3.get_object(Bucket=records_bucket, Key=file_name)
        return response_body

    except Exception as e:
        print(e)
        raise e

        return 0
