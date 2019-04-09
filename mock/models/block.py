from django.db import models


class Block(models.Model):
    blockHeader = models.ForeignKey("mock.BlockHeader", related_name="block", on_delete=models.CASCADE)
    transactions = models.ManyToManyField("mock.Transaction", related_name="blocks")
