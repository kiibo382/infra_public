import ast
import datetime
import json
import os

import boto3

TRANSCRIBE_BUCKET = os.environ["TRANSCRIBE_BUCKET_NAME"]
COMPREHEND_BUCKET = os.environ["COMPREHEND_BUCKET_NAME"]
# path を records/{records_bucket}/{year}/{month}/{day}/{hour}/{obj_name}にしても可。

def get(event, context):
    s3 = boto3.client("s3")
    try:
        records_bucket = event["pathParameters"]["records_bucket"]
        date_str = event["pathParameters"]["key"]

        # date_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

        date_dt = datetime.datetime.fromtimestamp(date_str)
        path = (
            records_bucket
            + "/"
            + str(date_dt.year)
            + "/"
            + str(date_dt.month)
            + "/"
            + str(date_dt.day)
            + "/"
            + str(date_dt.hour)
            + "/"
        )

        transcribe_response = s3.get_object(
            Bucket=TRANSCRIBE_BUCKET,
            Key=path + date_str + "-transcribe.json",
        )
        comprehend_response = s3.get_object(
            Bucket=COMPREHEND_BUCKET,
            Key=path + date_str + "-comprehend.json",
        )
        response_body = {
            "transcirbe_result": ast.literal_eval(transcribe_response["Body"].read().decode("UTF-8")),
            "comprehend_result": ast.literal_eval(comprehend_response["Body"].read().decode("UTF-8")),
        }

        return {
            "statusCode": 200,
            "body": json.dumps({"result": response_body}),
            "isBase64Encode": False,
            "headers": {
                "Content-Type": "application/json"
            },
        }

    except Exception as e:
        print(e)
        raise e
