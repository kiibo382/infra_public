rm packaged.yaml
sam package \
    --template-file binary.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket kizawa-lambda-code-bucket