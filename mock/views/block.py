from rest_framework import viewsets

from mock.models import Block
from mock.serializers.block import BlockSerializer


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
