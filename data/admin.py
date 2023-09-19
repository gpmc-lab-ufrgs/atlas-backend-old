from django.contrib import admin

from .models import Data_state
from .models import Data_city
from .models import Data_sector
from .models import Cnae
from .models import Cnae_munic

admin.site.register(Data_state)
admin.site.register(Data_city)
admin.site.register(Data_sector)
admin.site.register(Cnae)
admin.site.register(Cnae_munic)