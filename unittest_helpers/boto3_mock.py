import boto3
from botocore.stub import Stubber

def client(*args, **kwargs):
    client = boto3.client(*args, **kwargs)
    stub = Stubber(client)
    pass

def resource(*args, **kwargs):
    resource = boto3.resource(*args, **kwargs)
    pass