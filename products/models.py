from django.db import models

#ProductTypeModel
class ProductType(models.Model):
    STATUSES = {
        "active": "Active",
        "inactive": "Inactive"
    }
    name = models.CharField(max_length=511, null=False)
    status = models.CharField(max_length=55, choices=STATUSES)

    def __str__(self) -> str:
        return self.name
    
#Product
class Product(models.Model):
    type_product = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    product_name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=100)
    available = models.IntegerField(null=False)
    def __str__(self) -> str:
        return self.product_name
    
