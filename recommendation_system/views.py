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

class Recommendation_systemView(ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['post'])
    def recommendation_system(self, request):
        if request.method == 'POST':
            # Handle POST request

            # 1
            state = request.data.get('state')
            category = request.data.get('selectedCategory')
            description = request.data.get('selectedDescription')

            renda_cliente = request.data.get('sliderValue')
            aluguel = request.data.get('sliderValue2')
            # Process the state value or make the necessary API calls

            ###RECOMMENDATION ALGORITHM###

            selected_districts = District.objects.filter(SIGLA_UF=state)[:4]

            # 2

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
                'districts': districts_list
            }
            return JsonResponse(response_data)
        else:
            # Handle other HTTP methods or invalid requests
            response = HttpResponse("Method Not Allowed", status=405)
            return response


