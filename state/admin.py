from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from state.models import State

@admin.register(State)
class StateAdmin(OSMGeoAdmin):
    default_lat: 7495000
    default_lng: 1400000
    default_zoom: 12