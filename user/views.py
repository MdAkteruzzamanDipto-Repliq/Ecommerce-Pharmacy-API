from django.shortcuts import render

from rest_framework import generics

from core.models import User
from core import permissions

from .serializers import UserSerializer

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class GetAllUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsSuperuser]
    
