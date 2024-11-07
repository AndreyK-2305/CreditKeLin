# views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Credit, Payment
from .serializers import CreditSerializer, PaymentSerializer, CreditCreationSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ["status"]
    search_fields = ["client"]
    filterset_fields = ["status"]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreditCreationSerializer
        return CreditSerializer

    @action(detail=True, methods=['get'])
    def payments(self, request, pk=None):
        credit = self.get_object()
        payments = credit.payments.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["value"]
    filterset_fields = ["payment_STATUS"]
    permission_classes = [IsAuthenticated]
