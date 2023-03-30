from rest_framework import viewsets
from django.shortcuts import render

from .models import State
from .serializers import StateSerializer

from djgeojson.views import GeoJSONLayerView

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateGeoJson(GeoJSONLayerView):
    model = State
    geometry_field = 'geometry'
    properties = ['CD_UF', 'POPULATION', 'NM_UF', 'SIGLA_UF', 'NM_REGIAO']

    def get_properties(self, feature):
        return {
            "CD_UF": feature.CD_UF,
            "POPULATION": feature.POPULATION,
            "NM_UF": feature.NM_UF,
            "SIGLA_UF": feature.SIGLA_UF,
            "NM_REGIAO": feature.NM_REGIAO,
        }

#def states_js(request):
#    states = State.objects.all()
#    context = {
#        'object_list': states,
#    }
#    return render(request, 'poco/states_js.html', context)