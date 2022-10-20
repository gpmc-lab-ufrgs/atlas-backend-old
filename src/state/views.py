from rest_framework import viewsets

from .models import State
from .serializers import StateSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    # def get_queryset(self):
    #     queryset = State.objects.filter(owner=self.request.user)
    #     return queryset
    
    # def perform_create(self, serializer):
    #     serializer.save()