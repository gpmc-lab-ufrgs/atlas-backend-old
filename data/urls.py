from django.urls import path, include
from rest_framework_nested import routers

from . import views as v

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path('data_city/json/', v.DistrictDataJsonView.as_view(),name='district_data_geojson'),
    path('data_city_dicio/json/', v.DistrictData.as_view(), name='district_data'),
]