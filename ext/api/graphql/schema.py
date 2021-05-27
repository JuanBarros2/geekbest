from graphene import Schema

from .query import Query
from ..job.model_job import JobSchema
from ..candidate.model_candidate import CandidateSchema, TechnologySchema

schema = Schema(query=Query, types=[
                JobSchema, CandidateSchema, TechnologySchema])
