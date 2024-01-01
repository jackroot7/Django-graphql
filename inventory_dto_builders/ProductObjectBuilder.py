import graphene

from core.models import *
from inventory_dto.ProductObjects import *



class ProductObjectBuilder:
    
    @classmethod
    def get_category_data(self, id):
        category = ProductCategories.objects.filter(id=id).first()
        if category is None:
            return None
        
        return CategoryObject(
            id = category.id,
            category_name = category.category_name,
            category_is_active = category.category_is_active,
        )
