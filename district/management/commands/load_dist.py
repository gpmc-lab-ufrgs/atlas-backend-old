from district.models import District

import os
import json
from django.contrib.gis.geos import GEOSGeometry

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Import district geojson data'
    

    def handle(self, *args, **options):
        #District.objects.all().delete()


        folder = 'district/data'
        file_paths = os.listdir(folder)
        
        for path in file_paths:
            file_path = folder + '/' + path
            #if file_path == folder + '/' + 'RS_Municipios_2020.json': ###### comentar e identar

            if os.path.exists(file_path) is False:
                raise CommandError('File "%s" does not exist' % file_path)

            self.stdout.write(self.style.SUCCESS('Successfully, file exist "%s"' % file_path))
            self.stdout.write(self.style.WARNING('processing...'))

            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for feature in data['features']:

                    geo_type = feature['type']

                    geo_id = feature['properties']["CD_MUN"]
                    geo_name = feature['properties']["NM_MUN"]
                    geo_code = feature['properties']["SIGLA_UF"]
                    geo_region = feature['properties']["AREA_KM2"]
                    #geo_population = feature['properties']["POPULATION"]

                    if feature['geometry']['type'] == 'Polygon':
                        feature['geometry']['type'] = 'MultiPolygon'
                        feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]

                    geom = GEOSGeometry(str(feature['geometry']))

                    if geo_code == 'RS':
                        geo_population = feature['properties']["POPULATION"]

                        District.objects.create(
                            name=geo_name,
                            type=geo_type,
                            geometry=geom,
                            POPULATION=geo_population,
                            CD_MUN= geo_id,
                            NM_MUN= geo_name,
                            SIGLA_UF= geo_code,
                            AREA_KM2= geo_region
                        )
                    else:
                        District.objects.create(
                            name=geo_name,
                            type=geo_type,
                            geometry=geom,
                            POPULATION=None,
                            CD_MUN=geo_id,
                            NM_MUN=geo_name,
                            SIGLA_UF=geo_code,
                            AREA_KM2=geo_region
                        )

            self.stdout.write(self.style.HTTP_SUCCESS('"%s" loaded' % file_path))

        self.stdout.write(self.style.SUCCESS('Data loaded :D'))