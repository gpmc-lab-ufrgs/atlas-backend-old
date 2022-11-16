from django.urls import path, include
from rest_framework_nested import routers

from .views import DataStateViewSet, DataDistrictViewSet

router = routers.DefaultRouter()

router.register("state", DataStateViewSet, basename='Date state')
router.register("district", DataDistrictViewSet, basename='Date district')

urlpatterns = [
    path("", include(router.urls)),
]