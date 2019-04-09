from rest_framework import viewsets

from mock.models import State
from mock.serializers.state import StateSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
