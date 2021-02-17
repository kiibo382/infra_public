import boto3
import datetime
import os
import urllib.parse
import json
import base64


def lambda_handler(event, context):
    print json.dumps(event)

    try:
        s3 = boto3.resource("s3")
        bucket = s3.Bucket("bucketName")

        # バイナリがBase64にエンコードされているので、ここでデコード
        imageBody = base64.b64decode(event["body-json"])

        key = event["pathParameters"]["key"]
        # リクエストパスを組み合わせてKeyにする
        imagePath = event["params"]["path"]
        key = imagePath["key"] + "/" + imagePath["name"]
        print key

        bucket.put_object(Body=imageBody, Key=key)
        print "success!"

    except Exception as e:
        print "Error!"
        print e


def get(event, context):
    bucket = event["pathParameters"]["bucketname"]
    key = event["pathParameters"]["key"]
