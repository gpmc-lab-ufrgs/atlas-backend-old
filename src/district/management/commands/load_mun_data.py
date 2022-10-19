from district.models import District
from district_property.models import DistrictProperty

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
                
                geo_id = feature['properties']["CD_MUN"]
                geo_name = feature['properties']["NM_MUN"]
                geo_code = feature['properties']["SIGLA_UF"]
                geo_region = feature['properties']["AREA_KM2"]
                
                if feature['geometry']['type'] == 'Polygon':
                    feature['geometry']['type'] = 'MultiPolygon'
                    feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]
                    
                geom = GEOSGeometry(str(feature['geometry']))
                
                properties = DistrictProperty.objects.create(
                    CD_MUN= geo_id,
                    NM_MUN= geo_name,
                    SIGLA_UF= geo_code,
                    AREA_KM2= geo_region 
                )
                
                District.objects.create(
                    name=geo_name,
                    type=geo_type,
                    geometry=GEOSGeometry(geom),
                    properties=properties
                )
                
        self.stdout.write(self.style.SUCCESS('Data loaded :D'))
                