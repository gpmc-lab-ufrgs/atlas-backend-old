from rest_framework import viewsets

from .models import District
from .serializers import DistrictSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        sigla = self.request.query_params.get('sigla')
        queryset = District.objects.all()
        if sigla is not None:
            queryset = queryset.filter(ACRONYM_FU=sigla)
        return queryset
    