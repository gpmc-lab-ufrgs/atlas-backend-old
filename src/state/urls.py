from django.urls import include, path
from rest_framework_nested import routers

from .views import StateViewSet

router = routers.DefaultRouter()

router.register('geojson', StateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]