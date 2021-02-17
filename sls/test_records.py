import base64

import boto3


def get(event, context):
    s3 = boto3.resource("s3")
    records_bucket = event["pathParameters"]["records_bucket"]
    key = event["pathParameters"]["proxy"]
    try:
        records_obj = s3.Object(records_bucket, key)
        records_data = records_obj.get()
    except Exception as e:
        print("no such file in the bucket")
        raise e

    try:
        records_bytes = records_data["Body"].read()
        records_encode = base64.b64encode(records_bytes)
        records_decode_str = records_encode.decode()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "audio/*",
                # "Content-Disposition": 'attachment; filename="sample.mp3"',
                # "Content-Length": records_data["ContentLength"],
            },
            "body": records_decode_str,
            "isBase64Encoded": True,
        }
    except Exception as e:
        print(e)
        raise e


# def post(event, context):
#     fp = io.BytesIO(base64.b64decode(event["body"]))
#     environ = {"REQUEST_METHOD": "POST"}
#     event["headers"] = {
#         "content-type": event["headers"]["Content-Type"],
#         "content-length": event["headers"]["Content-Length"],
#     }

#     print(fp)
#     print(event["headers"])
#     fs = FieldStorage(fp=fp, environ=environ, headers=event["headers"])

#     print(fs)
#     print(type(fs))
#     for f in fs.list:
#         print(f.name, f.filename, f.type, f.value)
#     try:
#         # records_data = s3.put_object(
#         #     Bucket=records_bucket, Body=body, Key=key, ContentType="audio/mpeg"
#         # )
#         return {
#             "statusCode": 201,
#             "headers": {"Content-Type": "application/json"},
#             "body": json.dumps({"message": "ok", "data": event}),
#             "isBase64Encode": False,
#         }

#     except Exception as e:
#         print(e)
#         raise e