from django.urls import path, include
from rest_framework_nested import routers

from .views import DictionaryJsonView
from . import views as v

router = routers.DefaultRouter()

#router.register("geojson", StateViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('dictionary/json/', v.DictionaryJsonView.as_view(), name='dictionary_json'),
]