from district.models import District
from upload.models import Spreadsheet_register
from sectors.models import Sectors,SectorsSensus

import os
import json
from django.contrib.gis.geos import GEOSGeometry

import json
import pandas as pd

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import district geojson data'

    def handle(self, *args, **options):

        # Read the JSON file
        with open('/home/demori/PycharmProjects/atlas-of-opportunity/atlas-frontend/src/data/states/TO_Municipios_2020_009.json', 'r+') as f:
            data = json.load(f)

            # Read the Excel file
            df = pd.read_excel('/home/demori/Documentos/atlas/populacao_municipios.xlsx')

            # Loop through each row in the Excel file
            for index, row in df.iterrows():
                # Get the CD_MUN value
                cd_mun = str(row['cd_mun'])

                # Search for the corresponding JSON object
                for feature in data['features']:
                    if feature['properties']['CD_MUN'] == cd_mun:
                        # Add the POPULATION attribute to the properties
                        feature['properties']['POPULATION'] = int(row['populacao_estimada_2021'])

            # Reset the file pointer to the beginning of the file
            f.seek(0)

            # Write the updated JSON data to the file
            json.dump(data, f)

            # Truncate the file to the current position (to remove any remaining data)
            f.truncate()
