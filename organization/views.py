from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions as drf_permissions

from core.models import Organization, UserOrganization, User
from core import permissions as custom_permissions

from .serializers import (
    OrganizationSerializer, 
    UserOrganizationSerializer, 
    OwnerCreateOrganizationUserSerializer,
    AdminCreateOrganizationUserSerializer,
    ManagerCreateOrganizationUserSerializer,
    )
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
    permission_classes = [drf_permissions.IsAuthenticated, 
                        #   custom_permissions.IsOrganizationOwner,
                        #   custom_permissions.IsOrganizationAdmin,
                        #   custom_permissions.IsOrganizationManager,
                        #   custom_permissions.IsOrganizationStaff
                          ]
    
    # def get_object(self):
    #     return self.request.user
    
    def get_queryset(self):
        user = self.request.user
        orgs = UserOrganization.objects.filter(user=user).values_list('organization', flat=True)
        
        return Organization.objects.filter(id__in=orgs)
    
class ListOrganizationInternalMembersView(generics.ListAPIView):
    # queryset = UserOrganization.objects.filter()
    serializer_class = UserOrganizationSerializer
    permission_classes = [custom_permissions.IsOrganizationInternal]
    
    
    def get_queryset(self):
        user = self.request.user
        user_organizations = UserOrganization.objects.filter(user=user).values_list('organization', flat=True)
        return UserOrganization.objects.filter(organization__in=user_organizations)

# class OwnerCreateOrganizationUserView(generics.CreateAPIView):
class OwnerCreateOrganizationUserView(generics.CreateAPIView):
    serializer_class = OwnerCreateOrganizationUserSerializer
    permission_classes = [custom_permissions.IsOrganizationOwner]
    
class AdminCreateOrganizationUserView(generics.CreateAPIView):
    serializer_class = AdminCreateOrganizationUserSerializer
    permission_classes = [custom_permissions.IsOrganizationAdmin]

class ManagerCreateOrganizationUserView(generics.CreateAPIView):
    serializer_class = ManagerCreateOrganizationUserSerializer
    permission_classes = [custom_permissions.IsOrganizationManager]

