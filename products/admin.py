from django.contrib import admin


from .models import ProductType, Product

from credit.models import Credit, Payment
from users.models import User
# Register your models here.
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'Product_Name', 'Price' , 'Available', 'Description']
    search_fields = ['name', 'Description']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'Value', 'Payment_STATUS']
    search_fields = ['Payment_id']

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['id', 'Client_id', 'Status', 'Product_id']
    search_fields = ['Status',]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username','type']
    search_fields = ['name']