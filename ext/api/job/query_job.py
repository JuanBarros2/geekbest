from .model_job import JobSchema, JobModel
from graphene import ObjectType, Field, String, List, Argument


def none_to_default(**kwargs):
    return {k: v for k, v in kwargs.items() if len(v) != 0}


class JobQuery(ObjectType):
    job = Field(List(JobSchema), args={
        'city': Argument(
            List(String), default_value=[]),
        'technologies': Argument(
            List(String), default_value=[])})

    def resolve_job(root, info, city, technologies):
        return list(JobModel.objects(**none_to_default(technologies__in=technologies, city__in=city)))
