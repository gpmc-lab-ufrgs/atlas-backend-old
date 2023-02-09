from django.urls import include, path
from rest_framework_nested import routers

from .views import DistrictViewSet

router = routers.DefaultRouter()

router.register('geojson', DistrictViewSet, basename='District')

urlpatterns = [
    path('', include(router.urls)),
]