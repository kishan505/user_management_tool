"""
URL configuration for user_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# from rest_framework import routers
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions


# Define your API endpoints using DRF routers
# router = routers.DefaultRouter()

# Create a schema view for Swagger documentation
# schema_view = get_schema_view(
#     openapi.Info(
#         title="user management API",
#         default_version='v1',
#         description="API description",
#         # Add other optional parameters like terms_of_service, contact, etc.
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user_management_app.urls")),
    path('swagger/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
