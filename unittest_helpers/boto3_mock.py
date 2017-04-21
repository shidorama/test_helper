import boto3
from botocore.stub import Stubber

def get_client():
    stubber = {'stubber': None}

    def client(*args, **kwargs):
        clt = boto3.client(*args, **kwargs)
        stubber['stubber'] = Stubber(clt)
        return clt

    return stubber, client

def get_resource():
    stubber = {'stubber': None}

    def resource(*args, **kwargs):
        clt = boto3.resource(*args, **kwargs)
        stubber['stubber'] = Stubber(clt)
        return clt

    return stubber, resource
