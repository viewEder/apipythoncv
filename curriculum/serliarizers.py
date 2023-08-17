# importar las librerías necesarias:
from rest_framework import serializers
# Importamos los modelos de datos:
from .models import User
# Importar de autenticación de django
from django.contrib.auth import authenticate, get_user_model