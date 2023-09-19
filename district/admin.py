from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from district.models import District

@admin.register(District)
class DistrictAdmin(OSMGeoAdmin):
    default_lat: 7495000
    default_lng: 1400000
    default_zoom: 12

