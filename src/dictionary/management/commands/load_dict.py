import json
import os

from django.core.management.base import BaseCommand, CommandError

from dictionary.models import Dictionary


class Command(BaseCommand):
    help = 'Import dictionary geojson data'
    

    def handle(self, *args, **options):
        
        folder = 'dictionary/data'
        file_paths = os.listdir(folder)
        
        for path in file_paths:
            file_path = f'{folder}/{path}'
            
            if os.path.exists(file_path) is False:
                raise CommandError(f'File {file_path} does not exist')

            self.stdout.write(self.style.SUCCESS(f'Successfully, file exist {file_path}'))
            self.stdout.write(self.style.WARNING('processing...'))
        
            with open(file_path, 'r') as file:
                data = json.load(file)
                
                for item in data:
                    
                    agency = item['Agency']
                    name = item['Name']
                    description = item['Description']
                    label = item['Label']
                    unit = item['Unit']
                    format = item['Format']
                    classification = item['Classification']
                    
                    Dictionary.objects.create(
                        name= name,
                        agency= agency,
                        format= format,
                        classification= classification,
                        description= description,
                        label= label,
                        unit= unit
                    )
            
                    self.stdout.write(self.style.HTTP_SUCCESS(f'{name} loaded'))
                
        self.stdout.write(self.style.SUCCESS('Data loaded :D'))
                