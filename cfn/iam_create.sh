aws cloudformation create-stack --stack-name kizawa-iam-cfn \
--template-body file://iam.yaml \
--capabilities CAPABILITY_NAMED_IAM 