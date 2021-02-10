import boto3
import json
import base64
import io
from cgi import FieldStorage


def get(event, context):
    s3 = boto3.client(
        "s3",
        endpoint_url="http://localhost:4569",
        aws_access_key_id="S3RVER",
        aws_secret_access_key="S3RVER",
        region_name="ap-northeast-1",
    )
    path = event["pathParameters"]["path"].split("_", 1)
    records_bucket = path[0]
    key = path[1]
    print(records_bucket)
    print(key)

    try:
        records_data = s3.get_object(Bucket=records_bucket, Key=key)
        # return {
        #     "statusCode": 200,
        #     "body": records_data["Body"],
        #     "isBase64Encode": True,
        #     "headers": {"Content-Type": "audio/mpeg"},
        # }
        # print(records_data)
        # print(type(records_data["Body"].read()))
        # print(type(records_data["Body"].read().decode()))
        # print(len(records_data["Body"].read()))
        print(dir(records_data["Body"]))
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": records_data["ContentType"],
                "Content-Disposition": 'attachment; filename="sample.mp3"',
                "Content-Length": records_data["ContentLength"],
            },
            "body": base64.b64encode(records_data["Body"].read()).decode(),
        }

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
        # imageBody = base64.b64decode(event["body-json"])
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
