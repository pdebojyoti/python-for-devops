import boto3

client = boto3.client('s3')

response =  client.create_bucket(
    Bucket = 'tubun-boto3-demo',
)