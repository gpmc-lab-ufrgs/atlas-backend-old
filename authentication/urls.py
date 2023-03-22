from django.urls import path, include
from rest_framework_nested import routers
from .views import LoginView

# API URLs:
api_router = routers.DefaultRouter()
api_router.register("login", LoginView,  basename='Login')

urlpatterns = [
    path("", include(api_router.urls)),
]