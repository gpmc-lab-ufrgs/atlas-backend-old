import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.generic import View

from dictionary.models import Dictionary
from district.models import District
from state.models import State
from .models import Data_city, Data_state


class DistrictDataJsonView(View):
    def get(self, request, *args, **kwargs):
        district_data = Data_city.objects.all()
        data = json.loads(serialize('json', district_data, fields=('city', 'dictionary', 'value')))
        return JsonResponse(data, safe=False)

class DistrictData(View):
    def get(self, request):
        cd_mun = request.GET.get('cd_mun')
        districts = District.objects.filter(CD_MUN=cd_mun)
        district_data = {}
        for district in districts:
            dictionaries = Dictionary.objects.filter(dictionary_city__city=district)
            district_data[district.CD_MUN] = {
                "MUNICIPIO": district.name,
            }
            for dictionary in dictionaries:
                data_city = Data_city.objects.filter(city=district, dictionary=dictionary).values()
                if data_city:
                    district_data[district.CD_MUN][dictionary.name] = {
                        "value": data_city[0]["value"],
                        "format": dictionary.format,
                        "unit": dictionary.unit
                    }
                else:
                    district_data[district.CD_MUN][dictionary.name] = {
                        "value": None,
                        "format": dictionary.format,
                        "unit": dictionary.unit
                    }
        return JsonResponse(district_data, json_dumps_params={'ensure_ascii': False})

class StateData(View):
    def get(self, request):
        cd_uf = request.GET.get('cd_uf')
        states = State.objects.filter(CD_UF=cd_uf)
        state_data = {}
        for state in states:
            dictionaries = Dictionary.objects.filter(dictionary__state=state)
            state_data[state.CD_UF] = {
                "ESTADO": state.name,
            }
            for dictionary in dictionaries:
                data_state = Data_state.objects.filter(state=state, dictionary=dictionary).values()
                if data_state:
                    state_data[state.CD_UF][dictionary.name] = {
                        "value": data_state[0]["value"],
                        "format": dictionary.format,
                        "unit": dictionary.unit
                    }
                else:
                    state_data[state.CD_UF][dictionary.name] = {
                        "value": None,
                        "format": dictionary.format,
                        "unit": dictionary.unit
                    }
        return JsonResponse(state_data, json_dumps_params={'ensure_ascii': False})

