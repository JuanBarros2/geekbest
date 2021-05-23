
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene import ObjectType, Field

from ..job.query_job import JobQuery

class Query(JobQuery):
    pass
