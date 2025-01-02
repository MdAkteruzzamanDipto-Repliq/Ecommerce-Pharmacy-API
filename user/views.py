from django.shortcuts import render

from rest_framework import generics, authentication
from rest_framework import permissions as drf_permissions

from core.models import User
from core import permissions as custom_permissions

from .serializers import UserSerializer

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class GetAllUserView(generics.ListAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    permission_classes = [custom_permissions.IsSuperuser]
    
    
class GetAndUpdateMeUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [drf_permissions.IsAuthenticated]
    
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
    
