from rest_framework import viewsets

from mock.models import Transaction
from mock.serializers.transaction import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
