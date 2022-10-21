from django.urls import path, include
from rest_framework_nested import routers

from .views import DataStateViewSet

router = routers.DefaultRouter()

router.register("state", DataStateViewSet, basename='Date state')

urlpatterns = [
    path("", include(router.urls)),
]