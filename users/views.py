# Create your views here.
from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

    ordering_fields = ["name"]
    search_fields = ["name", "telefono", "cc"]
    filterset_fields = ["status"]