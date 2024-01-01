from graphene import Schema
from core.schema import Query as core_query
from core.views import Mutation as core_mutation

class Query(core_query):
    pass

class Mutation(core_mutation):
    pass


schema = Schema(query=Query, mutation=Mutation)
