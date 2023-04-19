from rest_framework import viewsets

from .models import District
from .serializers import DistrictSerializer

from djgeojson.views import GeoJSONLayerView

from django.db.models import Q
class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        sigla = self.request.query_params.get('sigla')
        queryset = District.objects.all()
        if sigla is not None:
            queryset = queryset.filter(SIGLA_UF=sigla)
        return queryset

class DistrictGeoJson(GeoJSONLayerView):
    model = District
    geometry_field = 'geometry'
    properties = ['CD_MUN', 'POPULATION', 'NM_MUN', 'SIGLA_UF', 'AREA_KM2']

    def get_queryset(self):
        return self.model.objects.filter(Q(SIGLA_UF='RS')) # return self.model.objects.filter(Q(SIGLA_UF='RS') | Q(SIGLA_UF='RJ')) filtra apenas os municípios do RS e RJ

    def get_properties(self, feature):
        return {
            "CD_MUN": feature.CD_MUN,
            "POPULATION": feature.POPULATION,
            "NM_MUN": feature.NM_UF,
            "SIGLA_UF": feature.SIGLA_UF,
            "AREA_KM2": feature.AREA_KM2,
        }