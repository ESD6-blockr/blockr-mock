from django.db import models
from rest_framework.fields import JSONField


class Transaction(models.Model):
    TYPES = (("S", "Stake"), ("C", "Coin"), ("D", "Data"))

    recipient = models.CharField(max_length=255)
    amount = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(choices=TYPES, default=1)
    sender = models.CharField(max_length=255)
    signature = models.CharField(max_length=255)
    block_hash = models.CharField(max_length=255)
    data = JSONField(allow_null=True)
