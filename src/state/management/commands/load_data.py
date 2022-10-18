from state.models import State
from state_property.models import StateProperty

import os
import json
from django.contrib.gis.geos import GEOSGeometry

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Import Geojson data'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        
        file_path = options['file_path']
        if os.path.exists(file_path) is False:
            raise CommandError('File "%s" does not exist' % file_path)

        self.stdout.write(self.style.SUCCESS('Successfully, file exist "%s"' % file_path))
        
        with open(file_path, 'r') as file:
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
                
                properties = StateProperty.objects.create(
                    CD_UF= geo_id,
                    POPULATION= geo_population,
                    NM_UF= geo_name,
                    SIGLA_UF= geo_code,
                    NM_REGIAO= geo_region 
                )
                
                State.objects.create(
                    name=geo_name,
                    type=geo_type,
                    geometry=GEOSGeometry(geom),
                    properties=properties
                )
                
        self.stdout.write(self.style.SUCCESS('Data loaded :D'))
                