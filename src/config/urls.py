"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Atlas-Backend",
        default_version='v1',
        description="Atlas-Backend REST API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("state/", include("state.urls")),
    path("district/", include("district.urls")),
    path("data/", include("data.urls")),
    
    # In the path: / (the root path), the api documentation is displayed according to 
    # the OpenAPI specification using Swagger to generate this documentation 
    # automatically
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]

