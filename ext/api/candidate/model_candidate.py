from mongoengine import Document
from mongoengine.fields import (
    StringField, ListField, IntField, BooleanField,
    EmbeddedDocument, EmbeddedDocumentField
)
from graphene_mongo import MongoengineObjectType
from graphene.relay import Node
from graphene import ObjectType, String, List



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
        
class FiltersSchema(ObjectType):
    city = List(String)
    experience =  List(String)
    technologies =  List(String)

