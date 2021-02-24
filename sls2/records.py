import base64
import datetime
import json
import os
import urllib.parse

import boto3


# path を records/{records_bucket}/{year}/{month}/{day}/{hour}/{obj_name}にしても可。
def get(event, context):
    s3 = boto3.client("s3")
    records_bucket = event["pathParameters"]["records_bucket"]
    date_str = event["pathParameters"]["key"]
    date_dt = datetime.datetime.fromtimestamp(date_str)
    path = (
        +str(date_dt.year)
        + "/"
        + str(date_dt.month)
        + "/"
        + str(date_dt.day)
        + "/"
        + str(date_dt.hour)
        + "/"
    )
    key = path + "/vpbx*-" + date_str + ".wav"

    try:
        records_data = s3.get_object(Bucket=records_bucket, Key=key)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "audio/mpeg",
                "Content-Disposition": 'attachment; filename="sample.mp3"',
            },
            "body": base64.b64encode(records_data["Body"].read()).decode("UTF-8"),
            "isBase64Encoded": True,
        }

    except Exception as e:
        print(e)
        raise e


# def post(event, context):
#     fp = io.BytesIO(base64.b64decode(event["body"]))
#     environ = {"REQUEST_METHOD": "POST"}
#     event["headers"] = {
#         "content-type": event["headers"]["Content-Type"],
#         "content-length": event["headers"]["Content-Length"],
#     }

#     print(fp)
#     print(event["headers"])
#     fs = FieldStorage(fp=fp, environ=environ, headers=event["headers"])

#     print(fs)
#     print(type(fs))
#     for f in fs.list:
#         print(f.name, f.filename, f.type, f.value)
#     try:
#         # records_data = s3.put_object(
#         #     Bucket=records_bucket, Body=body, Key=key, ContentType="audio/mpeg"
#         # )
#         return {
#             "statusCode": 201,
#             "headers": {"Content-Type": "application/json"},
#             "body": json.dumps({"message": "ok", "data": event}),
#             "isBase64Encode": False,
#         }

#     except Exception as e:
#         print(e)
#         raise e