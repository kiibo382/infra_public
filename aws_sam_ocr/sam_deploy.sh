sam deploy \
    --template-file packaged.yaml \
    --stack-name kizawa-aws-sam \
    --capabilities CAPABILITY_IAM \
    --region ap-northeast-1