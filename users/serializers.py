# importar las librerías necesarias:
from rest_framework import serializers
# Importamos los modelos de datos:
from .models import User

# Creamos la clase serializadora:
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # El modelo que vamos a usar es el del usuario (User)
        # fields = '__all__' # ('id', 'username','first_name')
        fields = [
            'id',
            'last_login',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'is_active',
            'date_joined',
            'email',
            'type_id',
            'identification',
            'photo',
            'country',
            'city',
            'address',
            'phone',
            'birthday',
            'occupation_job',
            'relocate'
        ]