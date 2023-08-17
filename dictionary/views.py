from rest_framework import viewsets
from django.shortcuts import render

from .models import Dictionary
#from .serializers import DictionarySerializer
from django.http import JsonResponse
from django.views import View
from .models import Dictionary


class DictionaryJsonView(View):
    def get(self, request, *args, **kwargs):
        title_order = [
            ('Demográfica', 'Demographic'),
            ('Economia', 'Economy'),
            ('Empreendedorismo', 'Entrepreneurship'),
            ('Educação', 'Education'),
            ('Saúde', 'Health'),
            ('Segurança', 'Safety'),
            ('Urbanismo', 'Urbanism'),
            ('Tecnologia e Inovação', 'Technology and inovation'),
            ('Meio Ambiente', 'Environment'),
            ('Mobilidade', 'Mobility'),
        ]

        dictionaries = Dictionary.objects.filter(ranking=1, table='city')
        groups = {title: {'title_english': title_en, 'content': []} for title, title_en in title_order}

        for dictionary in dictionaries:
            group_title = dictionary.new_classification_ptbr
            group_title_en = dictionary.new_classification_en
            if group_title in groups:
                item = {
                    'label': dictionary.name,
                    'title': dictionary.label_ptbr,
                    'title_en': dictionary.label_en,
                    'description': f"{dictionary.description_ptbr} - {dictionary.agency}",
                    'description_en': f"{dictionary.description_en} - {dictionary.agency}",
                    'format': dictionary.format,
                    'unit': dictionary.unit,
                    'type': dictionary.unit,
                }
                groups[group_title]['content'].append(item)

        data = []
        for group_title_ptbr, group_data in groups.items():
            if group_data['content']:
                data.append({'title': group_title_ptbr, **group_data})

        response = JsonResponse(data, json_dumps_params={'ensure_ascii': False}, safe=False)
        response['Content-Type'] = 'application/json; charset=utf-8'
        return response


class DictionaryStateJsonView(View):
    def get(self, request, *args, **kwargs):
        title_order = [
            ('Demográfica', 'Demographic'),
            ('Economia', 'Economy'),
            ('Empreendedorismo', 'Entrepreneurship'),
            ('Urbanismo', 'Urbanism'),
            ('Tecnologia e Inovação', 'Technology and inovation'),
        ]

        dictionaries = Dictionary.objects.filter(ranking=1, table='state')
        groups = {title: {'title_english': title_en, 'content': []} for title, title_en in title_order}

        for dictionary in dictionaries:
            group_title = dictionary.new_classification_ptbr
            group_title_en = dictionary.new_classification_en
            if group_title in groups:
                item = {
                    'label': dictionary.name,
                    'title': dictionary.label_ptbr,
                    'title_en': dictionary.label_en,
                    'description': f"{dictionary.description_ptbr} - {dictionary.agency}",
                    'description_en': f"{dictionary.description_en} - {dictionary.agency}",
                    'format': dictionary.format,
                    'unit': dictionary.unit,
                    'type': dictionary.unit,
                }
                groups[group_title]['content'].append(item)

        data = []
        for group_title_ptbr, group_data in groups.items():
            if group_data['content']:
                data.append({'title': group_title_ptbr, **group_data})

        response = JsonResponse(data, json_dumps_params={'ensure_ascii': False}, safe=False)
        response['Content-Type'] = 'application/json; charset=utf-8'
        return response




