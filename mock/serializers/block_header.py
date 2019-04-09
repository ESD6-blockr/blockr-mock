from rest_framework import serializers

from mock.models import BlockHeader


class BlockHeaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlockHeader
        fields = "__all__"
