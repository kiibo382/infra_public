import base64
import datetime
import io
import json
import os
import urllib.parse
from cgi import FieldStorage
import boto3


def get(event, context):
    s3 = boto3.resource(
        "s3",
        endpoint_url="http://localhost:4569",
        aws_access_key_id="S3RVER",
        aws_secret_access_key="S3RVER",
        region_name="ap-northeast-1",
    )
    records_bucket = event["pathParameters"]["records_bucket"]
    key = event["pathParameters"]["proxy"]
    try:
        records_obj = s3.Object(records_bucket, key)
        records_data = records_obj.get()
    except Exception as e:
        print("no such file in the bucket")
        raise e

    try:
        records_bytes = records_data["Body"].read()
        records_encode = base64.b64encode(records_bytes)
        records_decode_str = records_encode.decode()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "audio/*",
            },
            "body": records_decode_str,
            "isBase64Encoded": True,
        }
    except Exception as e:
        print(e)
        raise e


def post(event, context):
    s3 = boto3.resource(
        "s3",
        endpoint_url="http://localhost:4569",
        aws_access_key_id="S3RVER",
        aws_secret_access_key="S3RVER",
        region_name="ap-northeast-1",
    )

    encode_body = event["body"].encode()
    base64_body = base64.b64decode(encode_body)
    fp = io.BytesIO(base64_body)
    environ = {"REQUEST_METHOD": "POST"}
    event["headers"] = {
        "content-type": event["headers"]["Content-Type"],
        "content-length": event["headers"]["Content-Length"],
    }

    print(fp)

    fs = FieldStorage(fp=fp, environ=environ, headers=event["headers"])
    print(fs)

    for f in fs.list:
        print(f.name, f.filename, f.type, f.value)
    try:
        # s3.Object(bucket_name, key)
        # records_data = s3.upload_fileobj(fs)
        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "ok", "data": event["body"]}),
            "isBase64Encode": False,
        }

    except Exception as e:
        print(e)
        raise e
