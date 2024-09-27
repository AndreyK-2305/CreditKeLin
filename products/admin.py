from django.contrib import admin


from .models import ProductType, Product

# Register your models here.
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_id', 'Product_Name', 'Price' , 'Available', 'Description']
    search_fields = ['name', 'Description']