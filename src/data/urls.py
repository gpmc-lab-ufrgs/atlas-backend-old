from django.urls import include, path
from rest_framework_nested import routers

from .views import DataDistrictViewSet, DataStateViewSet

router = routers.DefaultRouter()

router.register('state', DataStateViewSet, basename='Date state')
router.register('district', DataDistrictViewSet, basename='Date district')

urlpatterns = [
    path('', include(router.urls)),
]