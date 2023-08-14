from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/products/', include('apps.products.urls')), # Urls
    path('api/productsv2/', include('drf.routers')), # Routers  

    path('api/auth/', obtain_auth_token),


]
