from rest_framework import permissions
from core.models import UserOrganization


class IsSuperuser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return request.user.is_superuser
    
class IsOrganizationInternal(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # userOrg = UserOrganization.objects.filter(user=request.user).values
        # if userOrg['role'] is not None:
        #     return userOrg
            
        return UserOrganization.objects.filter(user=request.user, role__in = ['owner', 'admin', 'manager', 'staff']).exists()
    
class IsOrganizationOwner(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return UserOrganization.objects.filter(user=request.user, role = 'owner').exists()
        
class IsOrganizationAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return UserOrganization.objects.filter(user=request.user, role = 'admin').exists()
    
class IsOrganizationManager(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return UserOrganization.objects.filter(user=request.user, role = 'manager').exists()
    
class IsOrganizationStaff(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return UserOrganization.objects.filter(user=request.user, role = 'staff').exists()
    

    

    

    