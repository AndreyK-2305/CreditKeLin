from django.contrib import admin
from .models import Payment, Credit

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'value', 'payment_STATUS']
    search_fields = ['Payment_id']

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'status', 'product']
    search_fields = ['Status']
