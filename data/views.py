import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.generic import View

from dictionary.models import Dictionary
from district.models import District
from .models import Data_city

class DistrictDataJsonView(View):
    def get(self, request, *args, **kwargs):
        district_data = Data_city.objects.all()
        data = json.loads(serialize('json', district_data, fields=('city', 'dictionary', 'value')))
        return JsonResponse(data, safe=False)

class DistrictData(View):
    def get(self, request):
        districts = District.objects.all()  # districts = District.objects.all()
        district_data = {}
        for district in districts:
            dictionaries = Dictionary.objects.filter(dictionary_city__city=district)
            district_data[district.CD_MUN] = {
                "MUNICIPIO": district.name,
            }
            for dictionary in dictionaries:
                data_city = Data_city.objects.filter(city=district, dictionary=dictionary).values()
                if data_city:
                    district_data[district.CD_MUN][dictionary.name] = data_city[0]["value"]
                else:
                    district_data[district.CD_MUN][dictionary.name] = None
        return JsonResponse(district_data)

