from django.contrib import admin


from .models import ProductType, Product, Payment, Credit, User

# Register your models here.
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_id', 'Product_Name', 'Price' , 'Available', 'Description']
    search_fields = ['name', 'Description']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['Payment_id', 'Value', 'Payment_STATUS']
    search_fields = ['Payment_id']

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['Credit_id', 'Client_id', 'Status','Created_at', 'Product_id']
    search_fields = ['Status',]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['Client_id', 'name', 'username','type']
    search_fields = ['name']