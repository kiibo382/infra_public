rm packaged.yaml
sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket kizawa-lambda-code-bucket