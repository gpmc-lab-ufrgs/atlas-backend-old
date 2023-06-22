from django.urls import path, include
from rest_framework_nested import routers
from .views import UploadView, CnpjView

# API URLs:
api_router = routers.DefaultRouter()
api_router.register("load_data", UploadView,  basename='Upload')

urlpatterns = [
    path("", include(api_router.urls)),
    path("cnpj_view/", CnpjView.cnpj, name='cnpj_view'),
]