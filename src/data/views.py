from rest_framework import viewsets

from .models import Data
from .serializers import DataSerializer

class DataStateViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializer

    def get_queryset(self):
        region_id = self.request.query_params.get('region_id')
        queryset = Data.objects.filter(type="state")
        if region_id is not None:
            queryset = queryset.filter(region_id=region_id)
        return queryset

    