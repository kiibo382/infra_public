import datetime
import json
import urllib.parse

import boto3

s3 = boto3.client("s3")
comprehend = boto3.client("comprehend")


def lambda_handler(event, context):
    transcribe_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    input_key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"], encoding="utf-8"
    )

    try:
        response = s3.get_object(Bucket=transcribe_bucket, Key=input_key)

        body = json.load(response["Body"])
        transcript = body["results"]["transcripts"][0]["transcript"]

        sentiment_response = comprehend.detect_sentiment(
            Text=transcript, LanguageCode="ja"
        )
    except Exception as e:
        print(e)
        print(
            "Error comprehend object {} in bucket {}".format(
                input_key, transcribe_bucket
            )
        )
        raise e

    comprehend_bucket = "kizawa-comprehend-bucket"
    output_key = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".json"

    try:
        upload_response = s3.put_object(
            Body=json.dumps(sentiment_response),
            Bucket=comprehend_bucket,
            Key=output_key,
        )
        print(upload_response)
    except Exception as e:
        print(e)
        print("Error upload comprehend data into s3 bucket.")
        raise e
