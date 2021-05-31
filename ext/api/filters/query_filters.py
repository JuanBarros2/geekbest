from .model_job import JobSchema, JobModel
from graphene import ObjectType, Field, String, List, Argument


class FiltersQuery(ObjectType):
    job = Field(List(JobSchema))

    def resolve_job(root, info, city, technologies):
        return list(
            JobModel.objects(
                **none_to_default(
                    technologies__in=technologies,
                    city__in=city)))
