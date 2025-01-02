from rest_framework import permissions

class IsSuperuser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return request.user.is_superuser
    