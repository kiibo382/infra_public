aws --endpoint="http://localhost:4569" \
    s3 cp tmp/sample.mp3 s3://kizawa-sample-dev-records-bucket1/sample.mp3 \
    --profile S3local