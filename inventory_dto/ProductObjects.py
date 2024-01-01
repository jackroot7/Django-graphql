import graphene
from inventory_dto.GlobalsObects import ResponseObject



class CategoryInputObject(graphene.InputObjectType):
    id = graphene.String()
    category_name = graphene.String(required=True)
    
    
class CategoryObject(graphene.ObjectType):
    id = graphene.String()
    category_name = graphene.String()
    category_is_active = graphene.Boolean()


class CategoryResponseObject(graphene.ObjectType):
    response = graphene.Field(ResponseObject)
    data = graphene.List(CategoryObject)
