import os

import pandas as pd

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import district geojson data'

    def handle(self, *args, **options):
        # Get the absolute path to the Excel file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        excel_file = os.path.join(current_directory, 'tabela-cnaes.xlsx')

        # Read the Excel file
        df = pd.read_excel(excel_file)

        # Group the data by 'NOME SETOR'
        grouped = df.groupby('NOME SETOR')

        # Create an empty dictionary to store the JSON data
        json_data = {}

        # Iterate over each group
        for group_name, group_data in grouped:
            # Convert the group data to a list of dictionaries
            group_list = group_data.to_dict(orient='records')
            # Add the group data to the JSON dictionary
            json_data[group_name] = group_list

        # Convert the JSON data to a JSON string with special character support
        json_string = pd.io.json.dumps(json_data, ensure_ascii=False)

        # Write the JSON string to a file with special character support
        with open('output.json', 'w', encoding='utf-8') as f:
            f.write(json_string)