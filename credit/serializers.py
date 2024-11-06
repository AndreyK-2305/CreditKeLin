from .models import Payment , Credit
from rest_framework import serializers


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):  #serializers.ModelSerializer

    class Meta:
        model = Payment
        fields = [' value','payment_STATUS', 'delayed_value']


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Credit
        fields = ['client', 'status', 'product', 'available', 'payment']