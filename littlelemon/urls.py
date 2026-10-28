"""
URL configuration for littlelemon project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Django Admin site
    path('admin/', admin.site.urls),

    # Root and Restaurant Application Routes
    path('', include('restaurant.urls')),
    path('restaurant/', include('restaurant.urls')),

    # Token Authentication Endpoint (DRF built-in)
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Djoser Authentication Endpoints (registration, token login, token logout)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
