from django.db import models

class ProductCategories(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=300, blank=True)
    category_is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'product_category_tbl'
        verbose_name = "01. Product Category"
    
    def __str__(self) -> str:
        return self.category_name


class ProductSupliers(models.Model):
    id = models.AutoField(primary_key=True)
    supliers_name = models.CharField(max_length=300, blank=True)
    
    class Meta:
        db_table = 'product_supliers_tbl'
        verbose_name = "02. Product Supliers"
    
    def __str__(self) -> str:
        return self.supliers_name




class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=300, blank=True)
    product_price = models.FloatField(default=0)
    product_stock_quantity = models.IntegerField(default=0)
    product_category = models.ForeignKey(ProductCategories,on_delete=models.RESTRICT, null=True, blank=True)
    product_is_active = models.BooleanField(default=True)
    product_registered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'products_tbl'
        verbose_name = "03. Products"
    
    def __str__(self) -> str:
        return self.product_name



class Purchases(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_quantity = models.IntegerField(default=0)
    purchase_suplier = models.ForeignKey(ProductSupliers,on_delete=models.RESTRICT, null=True, blank=True)
    purchase_product = models.ForeignKey(Product,on_delete=models.RESTRICT, null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'products_purchase_tbl'
        verbose_name = "04. Purchases"
    
    def __str__(self) -> str:
        return f"{self.purchase_quantity}: {self.purchase_product}: {self.purchase_suplier}"



class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    order_customer_name = models.CharField(max_length=300, blank=True)
    order_quantity = models.IntegerField(default=0)
    order_product = models.ForeignKey(Product,on_delete=models.RESTRICT, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'products_orders_tbl'
        verbose_name = "05. Orders"
    
    def __str__(self) -> str:
        return f"{self.order_customer_name}: {self.order_product}: {self.order_quantity}"


