aws --endpoint="http://localhost:4569" \
    s3 cp sample/sample.mp3 s3://kizawa-sample-dev-records-bucket1/sample.mp3 \
    --profile s3local

aws --endpoint="http://localhost:4569" \
    s3 cp sample/sample.wav s3://kizawa-sample-dev-records-bucket1/sample.wav \
    --profile s3local

aws --endpoint="http://localhost:4569" \
    s3 cp sample/sample-transcribe.json s3://kizawa-sample-dev-transcribe-bucket/kizawa-sample-dev-records-bucket1/sample-transcribe.json \
    --profile s3local

aws --endpoint="http://localhost:4569" \
    s3 cp sample/sample-comprehend.json s3://kizawa-sample-dev-comprehend-bucket/kizawa-sample-dev-records-bucket1/sample-comprehend.json \
    --profile s3local