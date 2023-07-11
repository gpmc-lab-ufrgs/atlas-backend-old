import smtplib
from datetime import date
from email.message import EmailMessage
from random import random

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
        selected_districts_list_final = []
        selected_states_list = []
        districts = []
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

            if state == 'BR':
                salario_medio = Dictionary.objects.get(name='x1685_10143_2020')
                data_state = Data_state.objects.filter(dictionary=salario_medio,
                                                       value__range=(int(renda_cliente), renda_cliente_max))

                for d in data_state:
                    selected_states_list.append(d.state)

                salario_medio_mun = Dictionary.objects.get(name='salario_medio_mensal_dos_trabalhadores_formais_2019')

                for state in selected_states_list:

                    districts = District.objects.filter(SIGLA_UF=state.SIGLA_UF)
                    for d in districts:
                        selected_districts_list.append(d)

                data_cities = Data_city.objects.filter(city__in=selected_districts_list,
                                                       dictionary=salario_medio_mun,
                                                       value__range=(int(renda_cliente), renda_cliente_max))
                for d in data_cities:
                    selected_districts_list_final.append(d.city)

                random_list = list(selected_districts_list_final)  # Create a copy of the list
                random_selection = random_list[:16]

                districts_list = [
                    {
                        'name': district.name+'/'+district.SIGLA_UF,
                        'CD_MUN': district.CD_MUN,
                        # Add more fields as needed
                    }
                    for district in random_selection
                ]

                # Return the result as a JSON response
                response_data = {
                    'districts': districts_list[:4]
                }

                return JsonResponse(response_data)

            else:
                selected_districts = District.objects.filter(SIGLA_UF=state)

                # 2
                salario_medio = Dictionary.objects.get(name='salario_medio_mensal_dos_trabalhadores_formais_2019')
                data_cities = Data_city.objects.filter(city__in=selected_districts,
                                         dictionary=salario_medio,
                                         value__range=(int(renda_cliente), renda_cliente_max))

            for d in data_cities:
                selected_districts_list.append(d.city)


            # Convert selected_districts to a list of dictionaries
            districts_list = [
                {
                    'name': district.name+'/'+district.SIGLA_UF,
                    'CD_MUN': district.CD_MUN,
                    # Add more fields as needed
                }
                for district in selected_districts_list
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


