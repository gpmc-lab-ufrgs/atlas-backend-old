from data.models import Data
from dictionary.models import Dictionary

import os
import json

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Import data geojson data'
    

    def handle(self, *args, **options):
        
        helper_folder = 'data/data/helper'
        helper_paths = os.listdir(helper_folder)
        
        
        for helper_path in helper_paths:
            helper = helper_folder + '/' + helper_path
            
            if os.path.exists(helper) is False:
                raise CommandError('File "%s" does not exist' % helper)

            self.stdout.write(self.style.SUCCESS('Successfully, file exist "%s"' % helper))
            self.stdout.write(self.style.NOTICE('Loading "%s" folder' % helper_path.replace(".json", "")))
            self.stdout.write(self.style.WARNING('processing...'))
            
        
            with open(helper, 'r') as file:
                helper_data = json.load(file)
                
                folder = 'data/data/' + helper_path.replace(".json", "")
                file_paths = os.listdir(folder)
                
                for path in file_paths:
                    file_path = folder + '/' + path
                    
                    if os.path.exists(file_path) is False:
                        raise CommandError('File "%s" does not exist' % file_path)

                    self.stdout.write(self.style.SUCCESS('file exist "%s"' % file_path))
                    self.stdout.write(self.style.WARNING('processing...'))
                    
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        
                        for id, item in enumerate(data):
                            
                            dictionary = Dictionary.objects.get(name=path.replace(".json", ""))
                          
                            Data.objects.create(
                                region_id=helper_data[id],
                                name=path.replace(".json", ""),
                                type=helper_path.replace(".json", ""),
                                value=item,
                                dictionary=dictionary,
                            )
                            
                    self.stdout.write(self.style.HTTP_SUCCESS('Folder "%s" loaded' % path.replace(".json", "")))
                    
            self.stdout.write(self.style.HTTP_SUCCESS('Folder "%s" loaded' % helper_path.replace(".json", "")))
                    
        self.stdout.write(self.style.SUCCESS('Data loaded :D'))
                