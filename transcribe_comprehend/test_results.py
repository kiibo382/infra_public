import ast
import json
import os

import boto3

TRANSCRIBE_BUCKET = os.environ["TRANSCRIBE_BUCKET_NAME"]
COMPREHEND_BUCKET = os.environ["COMPREHEND_BUCKET_NAME"]


def get(event, context):
    s3 = boto3.client(
        "s3",
        endpoint_url="http://localhost:4569",
        aws_access_key_id="S3RVER",
        aws_secret_access_key="S3RVER",
        region_name="ap-northeast-1",
    )
    try:
        records_bucket = event["pathParameters"]["records_bucket"]
        key = event["pathParameters"]["key"]

        transcribe_data = s3.get_object(
            Bucket=TRANSCRIBE_BUCKET,
            Key=records_bucket + "/" + key + "-transcribe.json",
        )
        transcribe_dict = ast.literal_eval(
            transcribe_data["Body"].read().decode("UTF-8")
        )
        transcribe_res = transcribe_dict["results"]["transcripts"]

        comprehend_data = s3.get_object(
            Bucket=COMPREHEND_BUCKET,
            Key=records_bucket + "/" + key + "-comprehend.json",
        )

        response_body = {
            "transcirbe_result": transcribe_res,
            "comprehend_result": ast.literal_eval(
                comprehend_data["Body"].read().decode("UTF-8")
            ),
        }

        return {
            "statusCode": 200,
            "body": json.dumps({"result": response_body}),
            "isBase64Encoded": False,
            "headers": {"Content-Type": "application/json"},
        }

    except Exception as e:
        print(e)
        raise e
