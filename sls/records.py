import base64

import boto3


def get(event, context):
    s3 = boto3.resource("s3")
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
