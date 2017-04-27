import boto3
from botocore.stub import Stubber

stubbers = []


def get_client(actions=None):
    stubber = {'stubber': None}
    for x in range(0, len(stubbers)):
        stubbers.pop()

    def client(*args, **kwargs):
        client_name = args[0]
        clt = boto3.client(*args, **kwargs)
        stbr = Stubber(clt)
        stubber['stubber'] = stbr
        stubbers.append((client_name, stbr))
        if actions:
            if isinstance(actions, list):
                if actions[0][0] == client_name:
                    actions_set = actions.pop(0)
                    for record in actions_set[1]:
                        getattr(stbr, record[0])(*record[1])
                    stbr.activate()
        return clt

    return stubber, client


def get_resource(actions=None):
    stubber = {'stubber': None}

    def resource(*args, **kwargs):
        resource_name = args[0]
        rsrc = boto3.resource(*args, **kwargs)
        stbr = Stubber(rsrc.meta.client)
        stubber['stubber'] = stbr
        stubbers.append((resource_name, stbr))
        if actions:
            if isinstance(actions, dict):
                actions_for_service = actions.get(resource_name)
                stub = stubber['stubber']
                for record in actions_for_service:
                    getattr(stub, record[0])(*record[1])
                stub.activate()
        return rsrc

    return stubber, resource
