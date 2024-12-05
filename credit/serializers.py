# serializers.py
from rest_framework import serializers
from .models import Payment, Credit
from decimal import Decimal
from datetime import datetime, timedelta

INTEREST_RATE = Decimal('0.05')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id", "value", "delayed_value", "payment_STATUS", "credit", "due_to")

    def update(self, instance: Payment, validated_data):
        credit = instance.credit
        previous_status = instance.payment_STATUS

        instance.payment_STATUS = validated_data.get('payment_STATUS', instance.payment_STATUS)
        instance.value = validated_data.get('value', instance.value)
        instance.delayed_value = validated_data.get('delayed_value', instance.delayed_value)
        instance.due_to = validated_data.get('due_to', instance.due_to)
        instance.save()

        if instance.payment_STATUS == "completed" and previous_status != "completed":
            credit.debt -= instance.value
            if credit.debt <= Decimal('0.00'):
                credit.status = "completed"
            credit.save()

        return instance

class CreditCreationSerializer(serializers.ModelSerializer):
    total_payments = serializers.IntegerField(write_only=True)

    class Meta:
        model = Credit
        fields = ['client', 'status', 'product', 'debt', 'total_payments']

    def create(self, validated_data):
        product = validated_data["product"]

        if product.available <= 0:
            raise serializers.ValidationError("No products in stock")
        product.available -= 1
        product.save()

        price = product.price
        n_payments = validated_data["total_payments"]
        
        interest = price * INTEREST_RATE * n_payments
        total_debt = price + interest

        payment_value = total_debt / n_payments
        validated_data["debt"] = total_debt
        validated_data["status"] = "active"
        credit = super().create(validated_data)

        # Verificación y depuración adicional
        print(f'Creating {n_payments} payments for credit {credit.id}.')

        for i in range(n_payments):
            due_date = datetime.now() + timedelta(days=30 * (i+1))  # Incrementar mensualmente
            payment = Payment.objects.create(
                credit=credit,
                value=payment_value,
                payment_STATUS="pending",
                delayed_value=payment_value * Decimal('1.1'),
                due_to=due_date,
            )
            print(f'Payment {payment.id} created for credit {credit.id} due on {due_date}.')

        return credit

class CreditSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    product_name = serializers.SlugRelatedField(source="product", read_only=True, slug_field="product_name")
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Credit
        fields = (
            "id", "client", "client_name", "product", "product_name", "status", "debt", "total_payments", "payments"
        )

    def get_client_name(self, obj):
        return obj.client.__str__()
