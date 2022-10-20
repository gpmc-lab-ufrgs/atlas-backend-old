from district.models import District

import os
import json
from django.contrib.gis.geos import GEOSGeometry

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Import district geojson data'
    

    def handle(self, *args, **options):
        
        folder = 'district/data'
        file_paths = os.listdir(folder)
        
        for path in file_paths:
            file_path = folder + '/' + path
            
            if os.path.exists(file_path) is False:
                raise CommandError('File "%s" does not exist' % file_path)

            self.stdout.write(self.style.SUCCESS('Successfully, file exist "%s"' % file_path))
            self.stdout.write(self.style.WARNING('processing...'))
        
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
                    
                    District.objects.create(
                        name=geo_name,
                        type=geo_type,
                        geometry=geom,
                        CD_MUN= geo_id,
                        NM_MUN= geo_name,
                        SIGLA_UF= geo_code,
                        AREA_KM2= geo_region
                    )
            
            self.stdout.write(self.style.HTTP_SUCCESS('"%s" loaded' % file_path))
                
        self.stdout.write(self.style.SUCCESS('Data loaded :D'))
                