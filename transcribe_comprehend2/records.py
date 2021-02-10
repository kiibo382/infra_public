import boto3
import datetime
import os
import urllib.parse
import json
import base64


def get(event, context):
    s3 = boto3.client("s3")
    path = event["pathParameters"]["path"].split("/", 1)
    records_bucket = path[0]
    key = path[1]
    # date_str = event["pathParameters"]["finished_timestamp"]
    # date_dt = datetime.datetime.fromtimestamp(date_str)
    # path = (
    #     +str(date_dt.year)
    #     + "/"
    #     + str(date_dt.month)
    #     + "/"
    #     + str(date_dt.day)
    #     + "/"
    #     + str(date_dt.hour)
    #     + "/"
    # )

    try:
        # imageBody = base64.b64decode(event["body-json"])
        records_data = s3.get_object(Bucket=records_bucket, Key=key)
        # Key=path + "vpbx*-" + date_str + ".wav"
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "audio/mpeg",
                "Content-Disposition": 'attachment; filename="sample.mp3"',
            },
            "body": base64.b64encode(records_data["Body"]).decode("utf-8"),
            "isBase64Encode": True,
        }

    except Exception as e:
        print(e)
        raise e
