from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    StringField, ListField, IntField,
    ObjectIdField, BooleanField,
    EmbeddedDocument, EmbeddedDocumentField
)
from graphene_mongo import MongoengineObjectType
from graphene.relay import Node


class TechnologyModel(EmbeddedDocument):
    name = StringField()
    is_main_tech = BooleanField()


class CandidateModel(Document):
    meta = {'collection': 'candidate'}
    id = IntField(primary_key=True)
    city = StringField()
    technologies = ListField(EmbeddedDocumentField(TechnologyModel))
    experience = StringField()


class TechnologySchema(MongoengineObjectType):

    class Meta:
        model = TechnologyModel


class CandidateSchema(MongoengineObjectType):

    class Meta:
        model = CandidateModel
        name = "Candidate"
        interfaces = (Node,)
