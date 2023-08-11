from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
# from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter() # Objeto para la creación de la ruta
# Implementación de ruta de usuarios:
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
]

