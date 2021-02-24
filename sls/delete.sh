aws s3 rm s3://${STACK_NAME}-${STAGE}-records-bucket1 --recursive
aws s3 rm s3://${STACK_NAME}-${STAGE}-records-bucket2 --recursive
sls remove