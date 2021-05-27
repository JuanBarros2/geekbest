from .model_candidate import CandidateSchema, CandidateModel
from graphene import ObjectType, Field, String, List, Argument
from utils.args import none_to_default


class CandidateQuery(ObjectType):
    candidate = Field(List(CandidateSchema), args={
        'city': Argument(
            List(String), default_value=[]),
        'experience': Argument(
            List(String), default_value=[]),
    })

    def resolve_candidate(root, info, city, experience):
        return list(
            CandidateModel.objects(
                **none_to_default(
                    city__in=city,
                    experience__in=experience)))
