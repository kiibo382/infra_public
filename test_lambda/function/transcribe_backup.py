import datetime
import sys
import urllib.parse

import boto3

s3 = boto3.client("s3")
transcribe = boto3.client("transcribe")


def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"], encoding="utf-8"
    )
    if not key:
        print("Error get object {} in bucket {}".format(key, bucket))
        sys.exit(1)

    try:
        transcribe.start_transcription_job(
            TranscriptionJobName=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            + "_Transcription",
            LanguageCode="ja-JP",
            Media={
                "MediaFileUri": "https://s3.ap-northeast-1.amazonaws.com/"
                + bucket
                + "/"
                + key
            },
            OutputBucketName="*Your Output Bucket*",
        )
    except Exception as e:
        print(e)
        print("Error transcribe object {} in bucket {}".format(key, bucket))
        raise e


# s3からオブジェクトを取ってくる際にどのエラーが想定されるか
# 1. バケットからオブジェクトを取得できない
# 2.
# 失敗した際に通知する、SNSに送る
