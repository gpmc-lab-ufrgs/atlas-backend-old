from state.models import State

import os
import json
from django.contrib.gis.geos import GEOSGeometry

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Import state geojson data'

    def handle(self, *args, **options):
        folder = 'state/data'
        file_paths = os.listdir(folder)
        
        for path in file_paths:
            file_path = folder + '/' + path
            
            if os.path.exists(file_path) is False:
                raise CommandError('File "%s" does not exist' % file_path)

            self.stdout.write(self.style.SUCCESS('Successfully, file exist "%s"' % file_path))
            self.stdout.write(self.style.WARNING('processing...'))
            
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for feature in data['features']:
            
                    geo_type = feature['type']
                    
                    geo_id = feature['properties']["CD_UF"]
                    geo_population = feature['properties']["POPULATION"]
                    geo_name = feature['properties']["NM_UF"]
                    geo_code = feature['properties']["SIGLA_UF"]
                    geo_region = feature['properties']["NM_REGIAO"]
                    
                    if feature['geometry']['type'] == 'Polygon':
                        feature['geometry']['type'] = 'MultiPolygon'
                        feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]
                        
                    geom = GEOSGeometry(str(feature['geometry']))
                    
                    State.objects.create(
                        name=geo_name,
                        type=geo_type,
                        geometry=geom,
                        CD_UF= geo_id,
                        POPULATION= geo_population,
                        NM_UF= geo_name,
                        SIGLA_UF= geo_code,
                        NM_REGIAO= geo_region 
                    )   
            
            self.stdout.write(self.style.HTTP_SUCCESS('"%s" loaded' % file_path))
                    
        self.stdout.write(self.style.SUCCESS('Data loaded :D'))
                