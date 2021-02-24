import datetime

a = {
    "ResponseMetadata": {
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "accept-ranges": "bytes",
            "content-type": "audio/mpeg",
            "last-modified": "Wed, 10 Feb 2021 05:10:53 GMT",
            "etag": '"18fc7f0024c99b45f741d528d0411086"',
            "content-length": "27944",
            "date": "Wed, 10 Feb 2021 05:50:50 GMT",
            "connection": "keep-alive",
            "keep-alive": "timeout=5",
        },
        "RetryAttempts": 0,
    },
    "AcceptRanges": "bytes",
    "LastModified": datetime.datetime(2021, 2, 10, 5, 10, 53, tzinfo=tzutc()),
    "ContentLength": 27944,
    "ETag": '"18fc7f0024c99b45f741d528d0411086"',
    "ContentType": "audio/mpeg",
    "Metadata": {},
    "Body": "<botocore.response.StreamingBody object at 0x7fda2deeda30>",
}
