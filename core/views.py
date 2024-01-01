from django.shortcuts import render
import graphene
from core.models import ProductCategories
from inventory_dto.GlobalsObects import ResponseObject
from inventory_dto.ProductObjects import *
from inventory_dto_builders.ProductObjectBuilder import ProductObjectBuilder



class AddNewCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInputObject()
        
    response = graphene.Field(ResponseObject)
    data = graphene.Field(CategoryObject)
    
    @classmethod
    def mutate(self, root, info, input):
        new_category = ProductCategories.objects.create(
            category_name = input.category_name
        )
        
        data = ProductObjectBuilder.get_category_data(id = new_category.id)
        
        return self(response = ResponseObject.get_response(id = "1"), data=data)



class UpdateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInputObject()
        
    response = graphene.Field(ResponseObject)
    data = graphene.Field(CategoryObject)
    
    @classmethod
    def mutate(self, root, info, input):
        if input.id is None:
            return self(response = ResponseObject.get_response(id = "2"))
            
        success = ProductCategories.objects.filter(id = input.id).update(
            category_name = input.category_name
        )
        
        if not success:
            return self(response = ResponseObject.get_response(id = "2"))
        
        data = ProductObjectBuilder.get_category_data(id = input.id)
        
        return self(response = ResponseObject.get_response(id = "1"), data=data)



class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.String(required = True)
        
    response = graphene.Field(ResponseObject)    
    @classmethod
    def mutate(self, root, info, id):
            
        category = ProductCategories.objects.filter(id = input.id).first()
        if not category:
            return self(response = ResponseObject.get_response(id = "2"))
        
        # This is valid only if you perfom soft delete on your data and constraint is RESTRICTED not CASCADING 
        category.category_is_active = False
        category.save()
        
        
        return self(response = ResponseObject.get_response(id = "1"))



class Mutation(graphene.ObjectType):
    create_product_category = AddNewCategory.Field()
    update_product_category = UpdateCategory.Field()
    delete_product_category = DeleteCategory.Field()
