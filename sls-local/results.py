import ast
import json
import os

import boto3

TRANSCRIBE_BUCKET_NAME = os.environ["TRANSCRIBE_BUCKET_NAME"]
COMPREHEND_BUCKET_NAME = os.environ["COMPREHEND_BUCKET_NAME"]


def get(event, context):
    s3 = boto3.resource(
        "s3",
        endpoint_url="http://localhost:4569",
        aws_access_key_id="S3RVER",
        aws_secret_access_key="S3RVER",
        region_name="ap-northeast-1",
    )
    records_bucket = event["pathParameters"]["records_bucket"]
    key = event["pathParameters"]["proxy"]

    try:
        transcribe_obj = s3.Object(
            TRANSCRIBE_BUCKET_NAME,
            records_bucket + "/" + key + "-transcribe.json",
        )
        transcribe_data = transcribe_obj.get()
        transcribe_dict = ast.literal_eval(
            transcribe_data["Body"].read().decode("UTF-8")
        )
        transcribe_res = transcribe_dict["results"]["transcripts"]
    except Exception as e:
        print("no such file in the transcribe bucket")
        raise e

    try:
        comprehend_obj = s3.Object(
            COMPREHEND_BUCKET_NAME, records_bucket + "/" + key + "-comprehend.json"
        )
        comprehend_data = comprehend_obj.get()
    except Exception as e:
        print("no such file in the comprehend bucket")
        raise e

    try:
        response_body = {
            "transcirbe_result": transcribe_res,
            "comprehend_result": ast.literal_eval(
                comprehend_data["Body"].read().decode("UTF-8")
            ),
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "isBase64Encoded": False,
            "headers": {"Content-Type": "application/json"},
        }

    except Exception as e:
        print(e)
        raise e
