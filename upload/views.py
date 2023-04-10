from datetime import date

import tablib
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

from district.models import District
from .models import *
from dictionary.models import *
from data.models import *

class UploadView(ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['post'])
    def upload(self, request, format=None):
        data = request.FILES['file']
        table = request.data.get('table')
        sheetType = request.data.get('sheetType') #dicionario ou data
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user) #get the user's authentication token if it exists, or create a new one if it doesn't

                #tratamento da planilha
                imported_data = tablib.Databook()  # declare the databook first
                imported_data.xlsx = data.read()

                ###Dicionario###
                if sheetType == 'dictionary':
                    for dataset in imported_data.sheets():
                        if dataset.title == 'atlas':
                            try:
                                #salva o registro da planilha
                                try:
                                    today = date.today()
                                    spreadsheet = Spreadsheet_register.objects.create(Sheet_name=data.name,Date=today, User=user)
                                except Exception as e:
                                    # handle any exceptions that may occur during registration
                                    print(f"Failed to register spreadsheet: {str(e)}")

                                #salva o dicionário
                                count_blank_lines = 0
                                for d in dataset:
                                    if d[0] == d[1] == d[2] == d[3] == d[4]\
                                            == d[5] == d[6] == d[7] == d[8] \
                                            == d[9] == d[10] == d[11] == d[12] \
                                            == None:
                                        count_blank_lines = count_blank_lines + 1
                                        if count_blank_lines == 6:
                                            break # caso encontre 1 linha em branco para
                                    else:
                                        Dictionary.objects.create(
                                            agency=d[0], name=d[1], id_sheet=d[2], description_en=d[3],
                                            description_ptbr=d[4], label_en=d[5], label_ptbr=d[6], unit=d[7],
                                            format=d[8], new_classification_ptbr=d[9], new_classification_en=d[10],
                                            ranking=d[11], table=table, Spreadsheet_register=spreadsheet)
                            except:
                                Spreadsheet_register.objects.latest('Id').delete() # se der erro, apaga o registro da planilha

                ###DATA STATE###
                elif sheetType == 'data' and table == 'state':
                    for dataset in imported_data.sheets():
                        if dataset.title == 'atlas':
                            try:
                                #salva o registro da planilha
                                try:
                                    today = date.today()
                                    spreadsheet = Spreadsheet_register.objects.create(Sheet_name=data.name,Date=today, User=user)
                                except Exception as e:
                                    # handle any exceptions that may occur during registration
                                    print(f"Failed to register spreadsheet: {str(e)}")

                                #salva cada célula a partir da segunda linha terceira coluna como um data no banco
                                count_blank_lines = 0
                                for d in dataset:
                                    if d[0] == d[1] == d[2] == d[3] == d[4] == d[5] == d[6] == None:
                                        count_blank_lines = count_blank_lines + 1
                                        if count_blank_lines == 6:
                                            break  # caso encontre 1 linha em branco para
                                    else:
                                        tcode = d[0]
                                        state = State.objects.get(CD_UF=tcode) # pega o estado da linha

                                        headers = dataset.headers  # Get the column headers as a list
                                        headers = headers[2:]  # Remove the first two headers (tcode,tname)
                                        for h in headers:
                                            value = d[headers.index(h)+2] # pega o valor da célula atual
                                            dictionary = Dictionary.objects.get(name=h) # pega o dicionário cprresponte à celula atual

                                            Data_state.objects.create(state=state, dictionary=dictionary,
                                                                      value=value, Spreadsheet_register=spreadsheet)
                            except:
                                Spreadsheet_register.objects.latest('Id').delete() # se der erro, apaga o registro da planilha

                ###DATA STATE###
                elif sheetType == 'data' and table == 'city':
                    for dataset in imported_data.sheets():
                        if dataset.title == 'atlas':
                            #try:
                            #salva o registro da planilha
                            try:
                                today = date.today()
                                spreadsheet = Spreadsheet_register.objects.create(Sheet_name=data.name,Date=today, User=user)
                            except Exception as e:
                                # handle any exceptions that may occur during registration
                                print(f"Failed to register spreadsheet: {str(e)}")

                            #salva cada célula a partir da segunda linha terceira coluna como um data no banco
                            count_blank_lines = 0
                            for d in dataset:
                                if d[0] == d[1] == d[2] == d[3] == d[4] == d[5] == d[6] == None:
                                    count_blank_lines = count_blank_lines + 1
                                    if count_blank_lines == 6:
                                        break  # caso encontre 1 linha em branco para
                                else:
                                    tcode = d[0]
                                    name = d[1]
                                    try:
                                        city = District.objects.get(CD_MUN=tcode)
                                    except District.DoesNotExist:
                                        print("Error: District matching query does not exist: "+ tcode + " - "+ name +"")# pega o estado da linha

                                    headers = dataset.headers  # Get the column headers as a list
                                    headers = headers[2:]  # Remove the first two headers (tcode,tname)
                                    for h in headers:
                                        value = d[headers.index(h)+2] # pega o valor da célula atual
                                        dictionary = Dictionary.objects.get(name=h) # pega o dicionário cprresponte à celula atual

                                        Data_city.objects.create(city=city, dictionary=dictionary,
                                                                  value=value, Spreadsheet_register=spreadsheet)
                            #except:
                                #Spreadsheet_register.objects.latest('Id').delete() # se der erro, apaga o registro da planilha


                return Response({'msg': 'Successful', 'usr_pk': user.id, 'usr_token': str(token.key)})
            else:
                return Response({'msg': 'Not active'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'msg': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)