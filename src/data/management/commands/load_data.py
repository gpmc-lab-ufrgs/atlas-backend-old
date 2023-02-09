import json
import os

from django.core.management.base import BaseCommand, CommandError

from data.models import Data
from dictionary.models import Dictionary


class Command(BaseCommand):
    help = 'Import data geojson data'
    

    def handle(self, *args, **options):
        
        helper_folder = 'data/data/helper'
        helper_paths = os.listdir(helper_folder)
        
        
        for helper_path in helper_paths:
            helper = f'{helper_folder}/{helper_path}'
            
            if os.path.exists(helper) is False:
                raise CommandError(f'File {helper} does not exist')

            self.stdout.write(self.style.SUCCESS(f'Successfully, file exist {helper}'))
            self.stdout.write(self.style.NOTICE(f'Loading {helper_path.replace(".json", "")} folder'))
            self.stdout.write(self.style.WARNING('processing...'))
            
        
            with open(helper, 'r') as file:
                helper_data = json.load(file)
                
                folder = f'data/data/{helper_path.replace(".json", "")}'
                file_paths = os.listdir(folder)
                
                for path in file_paths:
                    file_path = f'{folder}/{path}'
                    
                    if os.path.exists(file_path) is False:
                        raise CommandError(f'File {file_path} does not exist')

                    self.stdout.write(self.style.SUCCESS(f'file exist {file_path}'))
                    self.stdout.write(self.style.WARNING('processing...'))
                    
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        
                        for id, item in enumerate(data):
                            
                            dictionary = Dictionary.objects.get(name=path.replace('.json', ''))
                          
                            Data.objects.create(
                                region_id=helper_data[id],
                                name=path.replace('.json', ''),
                                type=helper_path.replace('.json', ''),
                                value=item,
                                dictionary=dictionary,
                            )
                            
                    self.stdout.write(self.style.HTTP_SUCCESS(f'Folder {path.replace(".json", "")} loaded'))
                    
            self.stdout.write(self.style.HTTP_SUCCESS(f'Folder {helper_path.replace(".json", "")} loaded'))
                    
        self.stdout.write(self.style.SUCCESS('Data loaded :D'))
                