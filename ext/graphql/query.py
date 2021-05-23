
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene import ObjectType, Field

from ..model.role import Role as RoleModel
from .resolver import resolve_role


class Role(MongoengineObjectType):

    class Meta:
        model = RoleModel
        interfaces = (Node,)


class Query(ObjectType):
    role = Field(Role, resolver=resolve_role)
