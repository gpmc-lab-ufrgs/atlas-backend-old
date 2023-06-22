from django.urls import path, include
from rest_framework_nested import routers
from .views import *

# API URLs:
api_router = routers.DefaultRouter()
api_router.register("load_recommendation", Recommendation_systemView,  basename='Recommendation_system')

urlpatterns = [
    path("", include(api_router.urls)),
]