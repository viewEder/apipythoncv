from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, CreateUserView, RetreiveUpdateUserView, CreateTokenView, CreateLinkView, CreateResumeView, RetrieveUpdateDestroyLinkView, RetrieveUpdateDestroyResumeView
# from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter() # Objeto para la creación de la ruta
# Implementación de ruta de usuarios:
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/create', CreateUserView.as_view()),
    path('usuarios/login', CreateTokenView.as_view()),
    path('usuarios/edit', RetreiveUpdateUserView.as_view()),
    # ------ Las vistas de Links y Resumes: ------
    path("usuarios/links/create", CreateLinkView.as_view()),
    path("usuarios/resume/create", CreateResumeView.as_view()),
    # path("usuarios/links/edit", RetrieveUpdateDestroyLinkView.as_view()),
    # path("usuarios/resume/edit", RetrieveUpdateDestroyResumeView.as_view()),
]

