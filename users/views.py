from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, AuthTokenSerializer, LinkSerializer, ResumeSerializer
from .models import User, Links, ResumeUser

# Create your views here.
# Clase para listar usuarios:
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() # Get all users from the database
    serializer_class = UserSerializer

# Clase para crear usuarios
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

# Clase para ver y actualizar usuario logueado (es decir: uno mismo):
class RetreiveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # Obtenemos el usuario logueado
    def get_object(self):
        return self.request.user

# Clase para crear autenticación por token:
class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

# ------------------------------------ Los otras Vistas ------------------------------------
class CreateLinkView(generics.CreateAPIView):
    serializer_class = LinkSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class RetrieveUpdateDestroyLinkView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LinkSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CreateResumeView(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class RetrieveUpdateDestroyResumeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
