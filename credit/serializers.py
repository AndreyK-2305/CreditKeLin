from rest_framework import serializers
from .models import Payment, Credit
from decimal import Decimal
from datetime import datetime

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id", "value", "delayed_value", "payment_STATUS", "credit")

    def update(self, instance: Payment, validated_data):
        credit = instance.credit
        previous_status = instance.payment_STATUS

        instance.payment_STATUS = validated_data.get('payment_STATUS', instance.payment_STATUS)
        instance.value = validated_data.get('value', instance.value)
        instance.delayed_value = validated_data.get('delayed_value', instance.delayed_value)
        instance.save()

        if instance.payment_STATUS == "completed" and previous_status != "completed":
            credit.debt -= instance.value
            if credit.debt <= Decimal('0.00'):
                credit.status = "completed"
            credit.save()

        return instance

class CreditCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = (
            "id", "client", "product", "status", "debt", "total_payments",
        )
        extra_kwargs = {"debt": {"read_only": True}, "status": {"read_only": True}}

    def create(self, validated_data):
        product = validated_data["product"]

        if product.stock <= 0:
            raise serializers.ValidationError("No products in stock")
        product.stock -= 1
        product.save()

        price = validated_data["product"].price
        n_payments = validated_data["total_payments"]
        payment_value = price / n_payments
        total_debt = payment_value * n_payments
        validated_data["debt"] = total_debt
        validated_data["status"] = "active"
        credit = super().create(validated_data)

        today = datetime.now()
        for i in range(1, n_payments + 1):
            due_to = today.replace(month=today.month + i)
            Payment.objects.create(
                credit=credit,
                value=payment_value,
                due_to=due_to,
                payment_STATUS="pending",
                delayed_value=payment_value * 1.1,
            )
        return credit

class CreditSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    product_name = serializers.SlugRelatedField(source="product", read_only=True, slug_field="name")
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Credit
        fields = (
            "id", "client", "client_name", "product", "product_name", "status", "debt", "total_payments", "payments"
        )

    def get_client_name(self, obj):
        return obj.client.__str__()
