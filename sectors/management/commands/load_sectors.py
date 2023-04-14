from sectors.models import Sectors

import os
import json
from django.contrib.gis.geos import GEOSGeometry

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import sectors geojson data'

    def handle(self, *args, **options):
        folder = 'sectors/data'
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

                    geo_id = feature['properties']["CD_SETOR"]
                    cd_setor = feature['properties']["CD_SIT"]
                    cd_sit = feature['properties']["CD_SIT"]
                    nm_sit = feature['properties']["NM_SIT"]
                    cd_uf = feature['properties']["CD_UF"]
                    nm_uf = feature['properties']["NM_UF"]
                    sigla_uf = feature['properties']["SIGLA_UF"]
                    cd_mun = feature['properties']["CD_MUN"]
                    nm_mun = feature['properties']["NM_MUN"]
                    cd_dist = feature['properties']["CD_DIST"]
                    nm_dist = feature['properties']["CD_SETOR"]
                    cd_subdist = feature['properties']["NM_DIST"]
                    nm_subdist = feature['properties']["CD_SUBDIST"]

                    if feature['geometry']['type'] == 'Polygon':
                        feature['geometry']['type'] = 'MultiPolygon'
                        feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]

                    geom = GEOSGeometry(str(feature['geometry']))

                    Sectors.objects.create(
                        geo_id=geo_id,
                        cd_setor=cd_setor,
                        cd_sit=cd_sit,
                        nm_sit=nm_sit,
                        cd_uf=cd_uf,
                        nm_uf=nm_uf,
                        sigla_uf=sigla_uf,
                        cd_mun=cd_mun,
                        nm_mun=nm_mun,
                        cd_dist=cd_dist,
                        nm_dist=nm_dist,
                        cd_subdist= cd_subdist,
                        nm_subdist= nm_subdist,
                        geom=geom
                    )

            self.stdout.write(self.style.HTTP_SUCCESS('"%s" loaded' % file_path))

        self.stdout.write(self.style.SUCCESS('Data loaded :D'))
