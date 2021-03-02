import base64
import datetime
import io
import json
import os
import urllib.parse
from cgi import FieldStorage
import boto3

s3 = boto3.resource(
    "s3",
    endpoint_url="http://localhost:4569",
    aws_access_key_id="S3RVER",
    aws_secret_access_key="S3RVER",
    region_name="ap-northeast-1",
)


def s3_return_body(bucket_name, key):
    res_obj = s3.Object(bucket_name, key)
    res_data = res_obj.get()
    body = res_data["Body"]
    return body


def get(event, context):
    records_bucket = event["pathParameters"]["records_bucket"]
    key = event["pathParameters"]["proxy"]
    try:
        body = s3_return_body(records_bucket, key)
    except Exception as e:
        print("no such file in the bucket")
        raise e

    try:
        records_bytes = body.read()
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
