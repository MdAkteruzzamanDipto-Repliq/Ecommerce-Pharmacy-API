from django.contrib import admin

from .models import User, Organization, UserOrganization

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['username', 'first_name', 'last_name', 'status']

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'email']
    
@admin.register(UserOrganization)
class UserOrganizationAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['user', 'organization', 'role']
