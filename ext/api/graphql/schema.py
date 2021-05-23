from graphene import Schema

from .query import Query
from ..job.model_job import JobSchema

schema = Schema(query=Query, types=[JobSchema])
