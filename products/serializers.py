from .models import ProductType, Product
from rest_framework import serializers


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):  #serializers.ModelSerializer

    class Meta:
        model = ProductType
        fields = ['name', 'status']


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ['product_name', 'price', 'description', 'available', 'type_product']