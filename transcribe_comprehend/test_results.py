import datetime
import os
import json

import boto3

TRANSCRIBE_BUCKET = os.environ["TRANSCRIBE_BUCKET_NAME"]
COMPREHEND_BUCKET = os.environ["COMPREHEND_BUCKET_NAME"]


def get(event, context):
    s3 = boto3.client("s3")
    try:
        records_bucket = event["queryStringParameters"]["records_bucket"]
        file_name = event["queryStringParameters"]["file_name"]

        transcribe_response = s3.get_object(
            Bucket=TRANSCRIBE_BUCKET,
            Key=records_bucket + "/" + file_name + "-transcribe.json",
        )
        comprehend_response = s3.get_object(
            Bucket=COMPREHEND_BUCKET,
            Key=records_bucket + "/" + file_name + "-comprehend.json",
        )
        response_body = {
            "transcirbe_result": transcribe_response["Body"].read(),
            "comprehend_result": comprehend_response["Body"].read(),
        }

        return {
            "statusCode": 200,
            "body": json.dumps({"result": response_body}),
            "isBase64Encode": False,
            "headers": {},
        }

    except Exception as e:
        print(e)
        raise e

        return 0
