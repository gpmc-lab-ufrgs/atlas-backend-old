from district.models import District
from upload.models import Spreadsheet_register
from sectors.models import Sectors,SectorsSensus

import os
import json
from django.contrib.gis.geos import GEOSGeometry

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import district geojson data'

    def handle(self, *args, **options):
        SectorsSensus.objects.all().delete()
        #Spreadsheet_register.objects.get(Id=27).delete()
        #District.objects.all().delete()