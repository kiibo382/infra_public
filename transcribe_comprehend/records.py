import boto3
import datetime
import os
import urllib.parse
import json
import base64


def get(event, context):
    s3 = boto3.client("s3")
    records_bucket = event["queryStringParameters"]["records_bucket"]
    date_str = event["queryStringParameters"]["finished_timestamp"]
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

    try:
        # imageBody = base64.b64decode(event["body-json"])
        response_body = s3.get_object(
            Bucket=records_bucket, Key=path + "vpbx*-" + date_str + ".wav"
        )
        return response_body

    except Exception as e:
        print(e)
        raise e

        return 0
