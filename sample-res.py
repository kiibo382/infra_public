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
{
    "transcirbe_result": [
        {
            "transcript": "\u30cf\u30f3\u30ba\u30aa\u30f3 \u9806\u8abf \u3067\u3059 \u304b \u624b \u3092 \u52d5\u304b\u3059 \u306e \u697d\u3057\u3044 \u3067\u3059 \u3088 \u306d"
        }
    ],
    "comprehend_result": {
        "Sentiment": "POSITIVE",
        "SentimentScore": {
            "Positive": 0.9825301766395569,
            "Negative": 0.00034822686575353146,
            "Neutral": 0.017063843086361885,
            "Mixed": 5.778960621682927e-05,
        },
        "KeyPhrases": [
            {
                "Score": 1.0,
                "Text": "\u30cf\u30f3\u30ba\u30aa\u30f3",
                "BeginOffset": 0,
                "EndOffset": 5,
            },
            {
                "Score": 0.9999998807907104,
                "Text": "\u624b",
                "BeginOffset": 14,
                "EndOffset": 15,
            },
        ],
    },
}