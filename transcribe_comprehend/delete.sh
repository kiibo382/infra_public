export AWS_SDK_LOAD_CONFIG=1
aws s3 rm s3://kizawa-sample-dev-records-bucket1 --recursive
aws s3 rm s3://kizawa-sample-dev-records-bucket2 --recursive
aws s3 rm s3://kizawa-sample-dev-transcribe-bucket --recursive
aws s3 rm s3://kizawa-sample-dev-comprehend-bucket --recursive
serverless remove -v