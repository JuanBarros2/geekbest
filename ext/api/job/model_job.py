from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    StringField, ListField, IntField
)
from graphene_mongo import MongoengineObjectType
from graphene.relay import Node


class JobModel(Document):
    meta = {'collection': 'job'}
    id = IntField(primary_key=True)
    city = StringField()
    experience = StringField()
    technologies = ListField(StringField())


class JobSchema(MongoengineObjectType):

    class Meta:
        model = JobModel
        name = "Job"
        interfaces = (Node,)
