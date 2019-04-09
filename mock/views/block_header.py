from rest_framework import viewsets

from mock.models import BlockHeader
from mock.serializers.block_header import BlockHeaderSerializer


class BlockHeaderViewSet(viewsets.ModelViewSet):
    queryset = BlockHeader.objects.all()
    serializer_class = BlockHeaderSerializer
