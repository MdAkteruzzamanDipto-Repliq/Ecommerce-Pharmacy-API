from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions as drf_permissions

from core.models import Organization
from core import permissions as custom_permissions

from .serializers import OrganizationSerializer
# Create your views here.

class CreateOrganizationView(generics.CreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [custom_permissions.IsSuperuser]

class ListOrganizationView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [custom_permissions.IsSuperuser]
    
# class RetrieveAndUpdateMeOrganizationView(generics.RetrieveUpdateAPIView):
#     serializer_class = OrganizationSerializer
    
class ListOrganizationPublicView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.filter(status = 'active')
    permission_classes = [drf_permissions.AllowAny]

    def get_serializer(self, *args, **kwargs):
        kwargs['exclude'] = ['email', 'trade_license', 'status']
        return super().get_serializer(*args, **kwargs)
    
class ListMeOrganizationView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [custom_permissions.IsOrganizationOwner]
    
    def get_object(self):
        return self.request.user
