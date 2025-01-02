from rest_framework import permissions


class IsSuperuser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return request.user.is_superuser
    
class IsOrganizationOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        user = self.request.user
        
    
# class Demo(permissions.BasePermission):
    