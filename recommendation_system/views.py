import smtplib
from datetime import date
from email.message import EmailMessage
import tablib
from django.http import HttpResponse
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

class Recommendation_systemView(ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['post'])
    def recommendation_system(self, request):
        if request.method == 'POST':
            # Handle POST request
            state = request.data.get('state')
            category = request.data.get('selectedCategory')
            description = request.data.get('selectedDescription')

            #SLIDER VALUE
            # O = 0
            # 1 = R$5K
            # 2 = R$10K
            # 3 = R$20K
            # 4 = R$30K
            # 5 = R$40K
            # 6 = R$50K
            # 7 = R$100K
            # 8 = R$200K
            # 9 = R$500K+

            renda_cliente = request.data.get('sliderValue')
            aluguel = request.data.get('sliderValue2')
            # Process the state value or make the necessary API calls

            response = HttpResponse()
        else:
            # Handle other HTTP methods or invalid requests
            response = HttpResponse("Method Not Allowed", status=405)


        return response


