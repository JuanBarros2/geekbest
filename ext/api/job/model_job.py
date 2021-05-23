from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    StringField,
)
from graphene_mongo import MongoengineObjectType
from graphene.relay import Node


class JobModel(Document):
    meta = {'collection': 'job'}
    city = StringField()


class JobSchema(MongoengineObjectType):

    class Meta:
        model = JobModel
        name = "Job"
        interfaces = (Node,)
