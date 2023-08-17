# importar las librerías necesarias:
from rest_framework import serializers
# Importamos los modelos de datos:
from .models import ResumeUser, Links
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
    
# ------------------------------------ Los otros Modelos ------------------------------------
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'

    def createLink(self, validated_data):
        link = Links.objects.create(validated_data)
        return link
          
    def updateLink(self, instance, valdated_data):
        link = Links.update(instance, valdated_data)
        return link
    
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUser
        fields = '__all__'

    def createLink(self, validated_data):
        resume = ResumeUser.objects.create(validated_data)
        return resume
          
    def updateLink(self, instance, valdated_data):
        resume = ResumeUser.update(instance, valdated_data)
        return resume