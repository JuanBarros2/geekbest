from .model_candidate import CandidateSchema, CandidateModel, FiltersSchema
from graphene import ObjectType, Field, String, List, Argument
from utils.args import none_to_default
from graphene import ObjectType, Field
from mongoengine.queryset.visitor import Q


class CandidateQuery(ObjectType):
    candidate = Field(List(CandidateSchema), args={
        'city': Argument(
            List(String), default_value=[]),
        'experience': Argument(
            List(String), default_value=[]),

        'technologies': Argument(
            List(String), default_value=[]),
    })
    filters = Field(FiltersSchema)

    def resolve_filters(root, info):
        agg = CandidateModel.objects
        result = {
            'city': agg.distinct('city'),
            'experience': agg.distinct('experience'),
            'technologies': agg.distinct('technologies.name')
        }
        for key in result:
            result[key].sort()
        return result

    def resolve_candidate(root, info, city, experience, technologies):
        return list(
            CandidateModel.objects.filter(
                **none_to_default(city__in=city, experience__in=experience,
                                  technologies__name__in=technologies
                                  )))
