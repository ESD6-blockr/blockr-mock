from django.db import models


class State(models.Model):
    public_key = models.CharField(max_length=255)
    coin = models.DecimalField(max_digits=10, decimal_places=2)
    stake = models.DecimalField(max_digits=10, decimal_places=2)
