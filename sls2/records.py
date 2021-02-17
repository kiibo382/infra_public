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
