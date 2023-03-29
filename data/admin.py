from django.contrib import admin

from .models import Data_state
from .models import Data_city

admin.site.register(Data_state)
admin.site.register(Data_city)