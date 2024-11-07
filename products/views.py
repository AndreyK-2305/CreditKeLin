# Create your views here.
from django.shortcuts import render
from .models import ProductType, Product
from rest_framework import viewsets
from .serializers import ProductTypeSerializer, ProductSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
        
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

    ordering_fields = ["name"]
    search_fields = ["name"]
    filterset_fields = ["status"]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

    ordering_fields = ["product_name", "price", "type_product"]
    search_fields = ["name", "description"]
    filterset_fields = ["type_product"]

