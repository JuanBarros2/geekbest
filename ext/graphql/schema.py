from graphene import Schema

from .query import Query, Role

schema = Schema(query=Query, types=[Role])
