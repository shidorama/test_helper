# Basic info
This is collection of helpers that can be used to make writing of unittests easier. 
There are 3 main helpers:

## Fixture loader for unittests 
Loads json with same name as main test file and provides access to it through `__data` property.
Data then can be loaded using `_get_data()` method. 
This method expects that json will have key with same name as test method.

## boto3 mock for aws
Provides client mock for aws, while also providing access to stubber, so it can be used to provide fixture data to mocked clients.

## pep8 test
Provides 2 classes for pep8 testing. 
One of them is automatic in sense that it will go through all of the project files 
and test it and it just needs to be imported. Other one can be used as base.
