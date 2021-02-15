import base64
from cgi import FieldStorage
import json
import io

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
    key = event["pathParameters"]["key"]

    try:
        records_obj = s3.Object(records_bucket, key)
        records_data = records_obj.get(
            ResponseContentEncoding="binary",
            ResponseContentType="audio/mpeg",
        )
        # print(records_data)
        with open("sample.mp3", "rb") as f:
            records_bytes = f.read()
        records_encode = base64.b64encode(records_bytes)
        print("encode")
        print(records_bytes)
        records_decode = records_encode.decode()
        print("decode")
        print(records_decode)

        # print(records_data["Body"].read())
        # print("####################################")
        # print(type(records_data["Body"].read()))
        # print("encode")
        # print(base64.b64encode(records_data["Body"].read()))
        # print("decode")
        # print(base64.b64decode(records_data["Body"].read()))
        # print("decode")
        # print(type(records_data["Body"].read().decode()))
        # print(records_data["Body"].read().decode())
        # print("finish")
        # print(len(records_data["Body"].read()))
        # print(dir(records_data["Body"]))
        # print(base64.b64encode(records_data["Body"].read(amt=records_data["ContentLength"])).decode('utf-8'))
        return {
            "statusCode": 200,
            "headers": {
                # "Content-Type": "audio/mpeg",
                # "Content-Disposition": 'attachment; filename="sample.mp3"',
                # "Content-Length": records_data["ContentLength"],
            },
            "body": str(records_encode),
            "isBase64Encode": True,
        }
        # http://localhost:3000/dev/records/kizawa-sample-dev-records-bucket1/sample.mp3

    except Exception as e:
        print(e)
        raise e


def post(event, context):
    fp = io.BytesIO(base64.b64decode(event["body"]))
    environ = {"REQUEST_METHOD": "POST"}
    event["headers"] = {
        "content-type": event["headers"]["Content-Type"],
        "content-length": event["headers"]["Content-Length"],
    }

    print(fp)
    print(event["headers"])
    fs = FieldStorage(fp=fp, environ=environ, headers=event["headers"])

    print(fs)
    print(type(fs))
    for f in fs.list:
        print(f.name, f.filename, f.type, f.value)
    try:
        # records_data = s3.put_object(
        #     Bucket=records_bucket, Body=body, Key=key, ContentType="audio/mpeg"
        # )
        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "ok", "data": event}),
            "isBase64Encode": False,
        }

    except Exception as e:
        print(e)
        raise e
