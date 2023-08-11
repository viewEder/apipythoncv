from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() # Get all users from the database
    serializer_class = UserSerializer