import datetime
import os
import json

import boto3

TRANSCRIBE_BUCKET = os.environ["TRANSCRIBE_BUCKET_NAME"]
COMPREHEND_BUCKET = os.environ["COMPREHEND_BUCKET_NAME"]


def get(event, context):
    s3 = boto3.client("s3")
    try:
        # audio_bucket = event["pathParameters"]["audio_bucket"]
        # date_str = event["pathParameters"]["finished_timestamp"]

        # date_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

        # date_dt = datetime.datetime.fromtimestamp(date_str)
        # path = (
        #     audio_bucket
        #     + "/"
        #     + str(date_dt.year)
        #     + "/"
        #     + str(date_dt.month)
        #     + "/"
        #     + str(date_dt.day)
        #     + "/"
        #     + str(date_dt.hour)
        #     + "/"
        # )
        path = event["pathParameters"]["path"]

        transcribe_response = s3.get_object(
            Bucket=TRANSCRIBE_BUCKET,
            Key=path + "-transcribe.json",
        )
        comprehend_response = s3.get_object(
            Bucket=COMPREHEND_BUCKET,
            Key=path + "-comprehend.json",
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
