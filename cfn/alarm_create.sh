aws cloudformation create-stack --stack-name kizawa-lambda-alarm-cfn \
    --template-body file://lambda_alarm.yaml \
    --capabilities CAPABILITY_NAMED_IAM 