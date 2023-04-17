from sectors.models import Sectors,SectorsSensus

import os
import json
from django.contrib.gis.geos import GEOSGeometry

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import sectors geojson data'

    def handle(self, *args, **options):
        folder = '/home/demori/sectors/data_sectors/'
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

                    id = feature['properties']["ID"]
                    cd_geocodi = feature['properties']["CD_GEOCODI"]
                    tipo = feature['properties']["TIPO"]
                    cd_geocodb = feature['properties']["CD_GEOCODB"]
                    nm_bairro = feature['properties']["NM_BAIRRO"]
                    cd_geocods = feature['properties']["CD_GEOCODS"]
                    nm_subdist = feature['properties']["NM_SUBDIST"]
                    cd_geocodd = feature['properties']["CD_GEOCODD"]
                    cd_geocodm = feature['properties']["CD_GEOCODM"]
                    nm_municip = feature['properties']["NM_MUNICIP"]
                    nm_micro = feature['properties']["NM_MICRO"]
                    nm_meso = feature['properties']["NM_MESO"]

                    if feature['geometry']['type'] == 'Polygon':
                        feature['geometry']['type'] = 'MultiPolygon'
                        feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]

                    geom = GEOSGeometry(str(feature['geometry']))

                    SectorsSensus.objects.create(
                        ID=id,
                        cd_geocodi=cd_geocodi,
                        tipo=tipo,
                        cd_geocodb=cd_geocodb,
                        nm_bairro=nm_bairro,
                        cd_geocods=cd_geocods,
                        nm_subdist=nm_subdist,
                        cd_geocodd=cd_geocodd,
                        cd_geocodm=cd_geocodm,
                        nm_municip=nm_municip,
                        nm_micro=nm_micro,
                        nm_meso=nm_meso,
                        geo_type=geo_type,
                        geom=geom
                    )

            self.stdout.write(self.style.HTTP_SUCCESS('"%s" loaded' % file_path))

        self.stdout.write(self.style.SUCCESS('Data loaded :D'))
