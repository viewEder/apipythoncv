from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, CreateUserView, RetreiveUpdateUSerView, CreateTokenView
# from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter() # Objeto para la creación de la ruta
# Implementación de ruta de usuarios:
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/create', CreateUserView.as_view()),
    path('usuarios/login', CreateTokenView.as_view()),
    path('usuarios/edit', RetreiveUpdateUSerView.as_view()),
]

