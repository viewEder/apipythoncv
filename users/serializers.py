# importar las librerías necesarias:
from rest_framework import serializers
# Importamos los modelos de datos:
from .models import User
# Importar de autenticación de django
from django.contrib.auth import authenticate, get_user_model

# Creamos la clase serializadora:
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model() # El modelo que vamos a usar es el del usuario (User)
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
        extra_kwargs = {'password': {'write_only':True}}

        def create(self, validated_data):
            return get_user_model.objects.create_user(**validated_data)
        
        def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            user = super().update(instance, validated_data)

            if password:
                user.set_password(password)
                user.save()
            
            return user
        

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    
    # Método de validación:
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request = self.context.get('request'),
            username = email, 
            password= password
        )

        if not user:
            raise serializers.ValidationError('No se puede autenticar', code = 'authorization')

        attrs['user'] = user
        return  attrs