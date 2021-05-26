from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    StringField, ListField, IntField, ObjectIdField
)
from graphene_mongo import MongoengineObjectType
from graphene.relay import Node


class JobModel(Document):
    meta = {'collection': 'job'}
    _id = IntField(primary_key=True)
    city = StringField()
    technologies = ListField(StringField())
    experience = StringField()


class JobSchema(MongoengineObjectType):

    class Meta:
        model = JobModel
        name = "Job"
        interfaces = (Node,)
