import smtplib
from datetime import date
from email.message import EmailMessage

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
from sectors.models import SectorsSensus

from django.shortcuts import render
from folium import plugins, folium

from folium.plugins import MarkerCluster

import pandas as pdS
from django.views.generic import TemplateView
import folium
import pandas as pd

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

                                        try:
                                            # Get a Dictionary object by name
                                            my_dict = Dictionary.objects.get(name=d[1])

                                            # Update the fields of the retrieved object
                                            my_dict.agency = d[0]
                                            my_dict.name = d[1]
                                            my_dict.id_sheet = d[2]
                                            my_dict.description_en = d[3]
                                            my_dict.description_ptbr = d[4]
                                            my_dict.label_en = d[5]
                                            my_dict.label_ptbr = d[6]
                                            my_dict.unit = d[7]
                                            my_dict.format = d[8]
                                            my_dict.new_classification_ptbr = d[9]
                                            my_dict.new_classification_en = d[10]
                                            my_dict.ranking = d[11]
                                            my_dict.table = table
                                            my_dict.Spreadsheet_register = spreadsheet

                                            # Save the changes to the database
                                            my_dict.save()

                                            print(f"Dictionary object with name {d[1]} updated successfully.")

                                        except Dictionary.DoesNotExist:
                                            Dictionary.objects.create(
                                                agency=d[0], name=d[1], id_sheet=d[2], description_en=d[3],
                                                description_ptbr=d[4], label_en=d[5], label_ptbr=d[6], unit=d[7],
                                                format=d[8], new_classification_ptbr=d[9], new_classification_en=d[10],
                                                ranking=d[11], table=table, Spreadsheet_register=spreadsheet)

                                # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                                # CONFIGURAR E-MAIL E SENHA
                                EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                                EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                                # CRIAR UM E-MAIL
                                msg = EmailMessage()
                                msg['Subject'] = 'ATLAS - IMPORT RESULT'
                                msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                                msg['To'] = user.email
                                msg.set_content("Your spreadsheet " +data.name+" was successfully imported.")

                                # ENVIAR UM E-MAIL
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                    smtp.send_message(msg)

                            except:
                                Spreadsheet_register.objects.latest('Id').delete() # se der erro, apaga o registro da planilha

                                # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                                # CONFIGURAR E-MAIL E SENHA
                                EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                                EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                                # CRIAR UM E-MAIL
                                msg = EmailMessage()
                                msg['Subject'] = 'ATLAS - IMPORT RESULT'
                                msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                                msg['To'] = user.email
                                msg.set_content(
                                    "An error occurred while importing your spreadsheet. Inform the team.")

                                # ENVIAR UM E-MAIL
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                    smtp.send_message(msg)

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

                                            try:
                                                # Get a Dictionary object by name
                                                my_dict = Data_state.objects.get(state=state, dictionary=dictionary)

                                                # Update the fields of the retrieved object
                                                my_dict.city = state
                                                my_dict.dictionary = dictionary
                                                my_dict.value = value
                                                my_dict.Spreadsheet_register = spreadsheet

                                                # Save the changes to the database
                                                my_dict.save()

                                                print(f"Data state object with state {state} and dictionary {dictionary} updated successfully.")
                                            except:

                                                Data_state.objects.create(state=state, dictionary=dictionary,
                                                                          value=value, Spreadsheet_register=spreadsheet)

                                # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                                # CONFIGURAR E-MAIL E SENHA
                                EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                                EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                                # CRIAR UM E-MAIL
                                msg = EmailMessage()
                                msg['Subject'] = 'ATLAS - IMPORT RESULT'
                                msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                                msg['To'] = user.email
                                msg.set_content("Your spreadsheet " +data.name+" was successfully imported.")

                                # ENVIAR UM E-MAIL
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                    smtp.send_message(msg)

                            except:
                                Spreadsheet_register.objects.latest('Id').delete() # se der erro, apaga o registro da planilha

                                # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                                # CONFIGURAR E-MAIL E SENHA
                                EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                                EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                                # CRIAR UM E-MAIL
                                msg = EmailMessage()
                                msg['Subject'] = 'ATLAS - IMPORT RESULT'
                                msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                                msg['To'] = user.email
                                msg.set_content(
                                    "An error occurred while importing your spreadsheet  " +data.name+". Inform the team.")

                                # ENVIAR UM E-MAIL
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                    smtp.send_message(msg)

                ###DATA CITY###
                elif sheetType == 'data' and table == 'city':
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

                                            #Verifica se já existe no banco, se sim atualiza senão cria um novo registro
                                            try:
                                                # Get a Dictionary object by name
                                                my_dict = Data_city.objects.get(city=city, dictionary=dictionary)

                                                # Update the fields of the retrieved object
                                                my_dict.city = city
                                                my_dict.dictionary = dictionary
                                                my_dict.value = value
                                                my_dict.Spreadsheet_register = spreadsheet

                                                # Save the changes to the database
                                                my_dict.save()

                                                print(f"Data city object with city {city} and dictionary {dictionary} updated successfully.")
                                            except:

                                                Data_city.objects.create(city=city, dictionary=dictionary,
                                                                          value=value, Spreadsheet_register=spreadsheet)

                                # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                                # CONFIGURAR E-MAIL E SENHA
                                EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                                EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                                # CRIAR UM E-MAIL
                                msg = EmailMessage()
                                msg['Subject'] = 'ATLAS - IMPORT RESULT'
                                msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                                msg['To'] = user.email
                                msg.set_content("Your spreadsheet " +data.name+" was successfully imported.")

                                # ENVIAR UM E-MAIL
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                    smtp.send_message(msg)

                            except:
                                Spreadsheet_register.objects.latest('Id').delete() # se der erro, apaga o registro da planilha

                                # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                                # CONFIGURAR E-MAIL E SENHA
                                EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                                EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                                # CRIAR UM E-MAIL
                                msg = EmailMessage()
                                msg['Subject'] = 'ATLAS - IMPORT RESULT'
                                msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                                msg['To'] = user.email
                                msg.set_content(
                                    "An error occurred while importing your spreadsheet " +data.name+". Inform the team.")

                                # ENVIAR UM E-MAIL
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                    smtp.send_message(msg)

                ###DATA SENSUS###
                elif sheetType == 'data' and table == 'sensus':
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
                                            break  # caso encontre 6 linhas em branco para
                                    else:
                                        cd_geocodi = d[0]
                                        #name = d[1]
                                        try:
                                            sector = SectorsSensus.objects.get(cd_geocodi=cd_geocodi)
                                        except SectorsSensus.DoesNotExist:
                                            print("Error: Sector matching query does not exist: "+ cd_geocodi + " ")# pega o estado da linha

                                        headers = dataset.headers  # Get the column headers as a list
                                        headers = headers[2:]  # Remove the first two headers (tcode,tname)
                                        for h in headers:
                                            value = d[headers.index(h)+2] # pega o valor da célula atual
                                            dictionary = Dictionary.objects.get(name=h) # pega o dicionário cprresponte à celula atual

                                            #Verifica se já existe no banco, se sim atualiza senão cria um novo registro
                                            try:
                                                # Get a sector object
                                                my_dict = Data_sector.objects.get(sector, dictionary=dictionary)

                                                # Update the fields of the retrieved object
                                                my_dict.cd_geocodi = cd_geocodi
                                                my_dict.dictionary = dictionary
                                                my_dict.value = value
                                                my_dict.Spreadsheet_register = spreadsheet

                                                # Save the changes to the database
                                                my_dict.save()

                                                print(f"Data sectors object with sector {cd_geocodi} and dictionary {dictionary} updated successfully.")
                                            except:

                                                Data_sector.objects.create(sector=sector, dictionary=dictionary,
                                                                          value=value, Spreadsheet_register=spreadsheet)

                                # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                                # CONFIGURAR E-MAIL E SENHA
                                EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                                EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                                # CRIAR UM E-MAIL
                                msg = EmailMessage()
                                msg['Subject'] = 'ATLAS - IMPORT RESULT'
                                msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                                msg['To'] = user.email
                                msg.set_content("Your spreadsheet " +data.name+" was successfully imported.")

                                # ENVIAR UM E-MAIL
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                    smtp.send_message(msg)

                            except:
                                Spreadsheet_register.objects.latest('Id').delete() # se der erro, apaga o registro da planilha

                                # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                                # CONFIGURAR E-MAIL E SENHA
                                EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                                EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                                # CRIAR UM E-MAIL
                                msg = EmailMessage()
                                msg['Subject'] = 'ATLAS - IMPORT RESULT'
                                msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                                msg['To'] = user.email
                                msg.set_content(
                                    "An error occurred while importing your spreadsheet " +data.name+". Inform the team.")

                                # ENVIAR UM E-MAIL
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                    smtp.send_message(msg)

                ###DATA cnaes###
                elif sheetType == 'data' and table == 'cnaes':
                    for dataset in imported_data.sheets():
                        if dataset.title == 'atlas':
                            try:
                                # salva o registro da planilha
                                try:
                                    today = date.today()
                                    spreadsheet = Spreadsheet_register.objects.create(Sheet_name=data.name,
                                                                                      Date=today, User=user)
                                except Exception as e:
                                    # handle any exceptions that may occur during registration
                                    print(f"Failed to register spreadsheet: {str(e)}")

                                # salva cada célula a partir da segunda linha terceira coluna como um data no banco
                                count_blank_lines = 0
                                for d in dataset:
                                    if d[0] == d[1] == d[2] == d[3] == None:
                                        count_blank_lines = count_blank_lines + 1
                                        if count_blank_lines == 6:
                                            break  # caso encontre 6 linhas em branco para
                                    else:
                                        cnae = d[0]
                                        descricao = d[1]
                                        cod_setor = d[2]
                                        nome_setor = d[3]
                                        try:
                                            cnae = Cnae.objects.get(cnae=cnae)

                                            cnae.descricao = descricao
                                            cnae.cod_setor = cod_setor
                                            cnae.nome_setor = nome_setor
                                            cnae.Spreadsheet_register = spreadsheet

                                            cnae.save()
                                        except Cnae.DoesNotExist:
                                            print(
                                                "Error: cnae matching query does not exist: " + str(cnae) + " ")  # pega o estado da linha

                                            Cnae.objects.create(cnae=cnae,
                                                               descricao=descricao,
                                                               cod_setor=cod_setor,
                                                               nome_setor=nome_setor,
                                                               Spreadsheet_register=spreadsheet)

                                # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                                # CONFIGURAR E-MAIL E SENHA
                                EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                                EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                                # CRIAR UM E-MAIL
                                msg = EmailMessage()
                                msg['Subject'] = 'ATLAS - IMPORT RESULT'
                                msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                                msg['To'] = user.email
                                msg.set_content(
                                    "Your spreadsheet " + data.name + " was successfully imported.")

                                # ENVIAR UM E-MAIL
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                    smtp.send_message(msg)

                            except:
                                Spreadsheet_register.objects.latest(
                                    'Id').delete()  # se der erro, apaga o registro da planilha


                            # ENVIAR E-MAIL COM O RESULTADO APÓS O TÉRMINO
                            # CONFIGURAR E-MAIL E SENHA
                            EMAIL_ADRESS = 'atlas.aws.ufrgs@gmail.com'
                            EMAIL_PASSWORD = 'cbcdjyoegauwoock'

                            # CRIAR UM E-MAIL
                            msg = EmailMessage()
                            msg['Subject'] = 'ATLAS - IMPORT RESULT'
                            msg['From'] = 'atlas.aws.ufrgs@gmail.com'
                            msg['To'] = user.email
                            msg.set_content(
                                "An error occurred while importing your spreadsheet " + data.name + ". Inform the team.")

                            # ENVIAR UM E-MAIL
                            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                                smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                                smtp.send_message(msg)



                return Response({'msg': 'Successful', 'usr_pk': user.id, 'usr_token': str(token.key)})
            else:
                return Response({'msg': 'Not active'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'msg': 'Error'}, status=status.HTTP_401_UNAUTHORIZED)


class CnpjView(TemplateView):
    template_name = 'cnpj_view.html'

    def cnpj(request):
        city = ''
        locations = []
        center = (-29.366135253947203, -52.890702293659515)
        locations.append(center)

        if request.method == 'POST':
            city = request.POST['County']

            city = city.lower()

            df = pd.read_excel(f'upload/files/{city}.xlsx')

            for _, row in df.iterrows():
                latitude = row['latitude']
                longitude = row['longitude']
                city_name = row['city_name']

                if latitude != '' and longitude != '' and not pd.isnull(latitude) and not pd.isnull(
                        longitude) and city_name == city:
                    location = (float(latitude), float(longitude))
                    locations.append(location)

            if locations == []:
                center = (-29.366135253947203, -52.890702293659515)
                locations.append(center)

        # center the map
        center = (-29.366135253947203, -52.890702293659515)

        # create a Folium map centred at the above location
        m = folium.Map(location=center, zoom_start=5, width=2100, height=1550)

        cluster = MarkerCluster(locations=locations).add_to(m)

        # Add custom base maps to folium
        basemaps = {
            'Google Maps': folium.TileLayer(
                tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                attr='Google',
                name='Google Maps',
                overlay=True,
                control=True
            ),
            'Google Satellite': folium.TileLayer(
                tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
                attr='Google',
                name='Google Satellite',
                overlay=True,
                control=True
            ),
            'Google Terrain': folium.TileLayer(
                tiles='https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
                attr='Google',
                name='Google Terrain',
                overlay=True,
                control=True
            ),
            'Google Satellite Hybrid': folium.TileLayer(
                tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
                attr='Google',
                name='Google Satellite',
                overlay=True,
                control=True
            ),
            'Esri Satellite': folium.TileLayer(
                tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                attr='Esri',
                name='Esri Satellite',
                overlay=True,
                control=True
            )
        }

        # Add custom basemaps
        basemaps['Google Maps'].add_to(m)
        basemaps['Google Satellite Hybrid'].add_to(m)

        # Add a layer control panel to the map.
        m.add_child(folium.LayerControl())

        # fullscreen
        plugins.Fullscreen().add_to(m)

        # GPS
        plugins.LocateControl().add_to(m)

        # Add the draw
        plugins.Draw(export=True, filename='data.geojson', position='topleft', draw_options=None,
                     edit_options=None).add_to(m)

        # mouse position
        fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        plugins.MousePosition(position='bottomleft', separator=' | ', prefix="Mouse:", lat_formatter=fmtr,
                              lng_formatter=fmtr).add_to(m)

        # Add measure tool
        plugins.MeasureControl(position='topright', primary_length_unit='meters', secondary_length_unit='miles',
                               primary_area_unit='sqmeters', secondary_area_unit='acres').add_to(m)

        map = m._repr_html_()

        path_info = request.META['PATH_INFO']
        path_info = path_info.replace('/dados/', '')

        context = {
            'header': 'cnpj_view',
            'path_info': path_info,
            'm': map
        }

        return render(request, 'cnpj_view.html', context)