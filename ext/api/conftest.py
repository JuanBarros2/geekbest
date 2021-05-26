import pytest
from graphene.test import Client
from ext.api.graphql.schema import schema
from mongoengine import connect


@pytest.fixture(scope='function')
def graphql():
    connect('testbestgeek',
            host='mongomock://localhost')
    return Client(schema)
