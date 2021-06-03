from .model_job import JobSchema, JobModel
from graphene import ObjectType, Field, String, List, Argument
from utils.args import none_to_default


class JobQuery(ObjectType):
    job = Field(List(JobSchema), args={
        'city': Argument(
            List(String), default_value=[]),
        'technologies': Argument(
            List(String), default_value=[])})
            
    def resolve_job(root, info, city, technologies):
        return list(
            JobModel.objects(
                **none_to_default(
                    technologies__in=technologies,
                    city__in=city)))