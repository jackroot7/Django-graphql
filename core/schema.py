import graphene
from core.models import ProductCategories
from inventory_dto.GlobalsObects import ResponseObject
from inventory_dto.ProductObjects import CategoryResponseObject
from inventory_dto_builders.ProductObjectBuilder import ProductObjectBuilder


class Query(graphene.ObjectType):
    get_product_category = graphene.Field(CategoryResponseObject)


    def resolve_get_product_category(self, info):
        category_ids = ProductCategories.objects.filter(category_is_active = True).only('id')
        
        category_list = list(map(lambda category: ProductObjectBuilder.get_category_data(category.id), category_ids))
        
        return info.return_type.graphene_type(response=ResponseObject.get_response(id='1'),data=category_list)
        
        
        
    