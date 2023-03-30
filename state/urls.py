from django.urls import path, include
from rest_framework_nested import routers

from .views import StateViewSet
from . import views as v

router = routers.DefaultRouter()

#router.register("geojson", StateViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('geojson/', v.StateGeoJson.as_view(),name='state_geojson'),
]