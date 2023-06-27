import smtplib
from datetime import date
from email.message import EmailMessage
import tablib
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
import json

from rest_framework.viewsets import ModelViewSet, ViewSet


from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from district.models import *
from dictionary.models import *
from data.models import *

class Recommendation_systemView(ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['post'])
    def recommendation_system(self, request):
        selected_districts_list = []
        if request.method == 'POST':
            # Handle POST request

            # 1
            state = request.data.get('state')
            category = request.data.get('selectedCategory')
            description = request.data.get('selectedDescription')

            renda_cliente = request.data.get('sliderValue')
            renda_cliente_max = int(renda_cliente) + 1
            aluguel = request.data.get('sliderValue2')
            # Process the state value or make the necessary API calls

            ###RECOMMENDATION ALGORITHM###

            selected_districts = District.objects.filter(SIGLA_UF=state)

            # 2
            salario_medio = Dictionary.objects.get(name='salario_medio_mensal_dos_trabalhadores_formais_2019')
            #data_cities = Data_city.objects.filter(city__in=selected_districts,
            #                         dictionary=salario_medio,
            #                         value__range=(int(renda_cliente), int(renda_cliente_max)))

            #for d in data_cities:
            #    selected_districts_list.append(d.city)


            # Convert selected_districts to a list of dictionaries
            districts_list = [
                {
                    'name': district.name,
                    'CD_MUN': district.CD_MUN,
                    # Add more fields as needed
                }
                for district in selected_districts
            ]

            # Return the result as a JSON response
            response_data = {
                'districts': districts_list[:4]
            }
            return JsonResponse(response_data)
        else:
            # Handle other HTTP methods or invalid requests
            response = HttpResponse("Method Not Allowed", status=405)
            return response


