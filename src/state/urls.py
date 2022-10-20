from django.urls import path, include
from rest_framework_nested import routers

from .views import StateViewSet

router = routers.DefaultRouter()

router.register("geojson", StateViewSet)

urlpatterns = [
    path("", include(router.urls)),
]