from rest_framework import serializers

from mock.models import Block


class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"
