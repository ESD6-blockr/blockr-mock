from django.db import models


class BlockHeader(models.Model):
    version = models.DecimalField(default=1.00, decimal_places=2, max_digits=10)
    block_number = models.IntegerField()
    validator = models.CharField(max_length=255, default='XXXXXXXXXXXXXX')
    date = models.DateTimeField(auto_now_add=True)
    block_reward = models.DecimalField(default=10.00, decimal_places=2, max_digits=10)
    block_hash = models.CharField(primary_key=True, max_length=255)
    parent_hash = models.ForeignKey('mock.BlockHeader', related_name='child_hash', on_delete=models.CASCADE)
