from .model_job import JobSchema, JobModel
from graphene import ObjectType, Field, String, List, Argument


class JobQuery(ObjectType):
    job = Field(List(JobSchema), pagination=Argument(
        String, default_value=""))

    def resolve_job(root, info, pagination):
        return list(JobModel.objects.all())
