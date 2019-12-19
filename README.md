# kinesis_example

This is an example of a kinesis worker. It will have the following:
   - Consume from kinesis stream
   - Upon error, halt and retry
   - Upon error in retry, fail and raise hell
   - Example stream

## Permissions

```
source ./.keyfile
echo [Credentials] > ~/.boto
echo aws_access_key_id = $AWS_ACCESS_KEY >> ~/.boto
echo aws_secret_access_key = $AWS_SECRET_ACCESS_KEY >> ~/.boto
```

## Source
Started from AWS KCL python repo samples: `https://github.com/awslabs/amazon-kinesis-client-python`
