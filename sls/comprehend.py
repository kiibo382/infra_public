from __future__ import print_function
import json
import os
import urllib.parse

import boto3

s3 = boto3.client("s3")
comprehend = boto3.client("comprehend")
TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]


def lambda_handler(event, context):
    transcribe_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    input_key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"], encoding="utf-8"
    )

    try:
        response = s3.get_object(Bucket=transcribe_bucket, Key=input_key)
        body = json.load(response["Body"])

        transcript = ""
        for i in body["results"]["transcripts"]:
            transcript += i["transcript"]

        sentiment_response = comprehend.detect_sentiment(
            Text=transcript, LanguageCode="ja"
        )
        key_phrases = comprehend.detect_key_phrases(Text=transcript, LanguageCode="ja")
    except Exception as e:
        print(
            "Error comprehend object {} in bucket {}".format(
                input_key, transcribe_bucket
            )
        )
        print(e)
        raise e

    COMPREHEND_BUCKET = os.environ["COMPREHEND_BUCKET_NAME"]
    output_key = input_key.replace("transcribe", "comprehend")
    res_dict = {
        "Sentiment": sentiment_response["Sentiment"],
        "SentimentScore": sentiment_response["SentimentScore"],
        "KeyPhrases": key_phrases["KeyPhrases"],
    }

    try:
        s3.put_object(
            Body=json.dumps(res_dict), Bucket=COMPREHEND_BUCKET, Key=output_key
        )
    except Exception as e:
        print("Error upload comprehend data into s3 bucket.")
        print(e)
        raise e

    try:
        sns = boto3.resource("sns")
        topic = sns.Topic(TOPIC_ARN)
        message = {
            "default": "hello",
            "record_path": output_key.replace("-comprehend.json", ".wav"),
            "result_path": output_key.replace("-comprehend.json", ""),
        }
        messageJSON = json.dumps(message)
        topic.publish(Message=messageJSON, MessageStructure="json")
    except Exception as e:
        print("Error send message to SNS")
        print(e)
        raise e
