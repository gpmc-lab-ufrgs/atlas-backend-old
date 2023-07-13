from rest_framework import viewsets
from django.shortcuts import render

from .models import Dictionary
#from .serializers import DictionarySerializer
from django.http import JsonResponse
from django.views import View
from .models import Dictionary

class DictionaryJsonView(View): # cria o json dos dicionários separados por classificação
    def get(self, request, *args, **kwargs):
        dictionaries = Dictionary.objects.filter(ranking=1, table='city')
        groups = {}
        for dictionary in dictionaries:
            group_title = dictionary.new_classification_ptbr
            if group_title not in groups:
                groups[group_title] = []
            item = {
                'label': dictionary.name,
                'title': dictionary.label_ptbr,
                'title_en': dictionary.label_en,
                'description': f"{dictionary.description_ptbr} - {dictionary.agency}",
                'description_en': f"{dictionary.description_en} - {dictionary.agency}",
                'format': dictionary.format,
                'unit': dictionary.unit,
                'type': dictionary.unit,
                'group_title_en': dictionary.new_classification_en,
            }
            groups[group_title].append(item)
        data = []
        for group_title, content in groups.items():
            group_data = {'title': group_title, 'content': content}
            data.append(group_data)
        response = JsonResponse(data, json_dumps_params={'ensure_ascii': False}, safe=False)
        response['Content-Type'] = 'application/json; charset=utf-8'
        return response



