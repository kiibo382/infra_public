import boto3

s3 = boto3.resource(
    "s3",
    endpoint_url="http://localhost:4569",
    aws_access_key_id="S3RVER",
    aws_secret_access_key="S3RVER",
    region_name="ap-northeast-1",
)
