from rest_framework import serializers

from mock.models import State


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = "__all__"
