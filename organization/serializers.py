from rest_framework import serializers

from core.models import Organization, UserOrganization, User
from core.choices import OwnerRoleChoices, AdminRoleChoices, ManagerRoleChoices

class OrganizationSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    
    class Meta:
        model = Organization
        fields = ['name', 'email', 'phone', 'trade_license', 'address', 'thana', 'city', 'postal_code', 
                  'country', 'logo', 'description', 'status', 'role']
        
    def get_role(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user_organization = UserOrganization.objects.filter(
                user=request.user,
                organization=obj
            ).first()
            if user_organization:
                return user_organization.role
        return None
        
    def __init__(self, *args, **kwargs):
        exclude = kwargs.pop('exclude', None)
        super().__init__(*args, **kwargs)
        if exclude:
            for field in exclude:
                self.fields.pop(field, None)
                
class UserOrganizationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username')
    org_name = serializers.CharField(source = 'organization.name')
    # role = serializers.ChoiceField(choices=OwnerRoleChoices.CHOICES)
    class Meta:
        model = UserOrganization
        fields = ['username', 'org_name', 'role', 'status', 'salary']

class OwnerCreateOrganizationUserSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username')
    org_name = serializers.CharField(source='organization.name')
    role = serializers.ChoiceField(choices=OwnerRoleChoices.CHOICES) 
    class Meta:
        model = UserOrganization
        fields = ['username', 'org_name', 'role', 'status', 'salary']

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        username = user_data.get('username')

        organization_data = validated_data.pop('organization')
        org_name = organization_data.get('name')

        user, created = User.objects.get_or_create(username=username)
        organization, created = Organization.objects.get_or_create(name=org_name)
                
        organization_user = UserOrganization.objects.create(user=user, organization=organization, **validated_data)
        return organization_user

class AdminCreateOrganizationUserSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username')
    org_name = serializers.CharField(source='organization.name')
    role = serializers.ChoiceField(choices=AdminRoleChoices.CHOICES) 
    class Meta:
        model = UserOrganization
        fields = ['username', 'org_name', 'role', 'status', 'salary']

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        username = user_data.get('username')

        organization_data = validated_data.pop('organization')
        org_name = organization_data.get('name')

        user, created = User.objects.get_or_create(username=username)
        organization, created = Organization.objects.get_or_create(name=org_name)
                
        organization_user = UserOrganization.objects.create(user=user, organization=organization, **validated_data)
        return organization_user
    
class ManagerCreateOrganizationUserSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username')
    org_name = serializers.CharField(source='organization.name')
    role = serializers.ChoiceField(choices=ManagerRoleChoices.CHOICES) 
    class Meta:
        model = UserOrganization
        fields = ['username', 'org_name', 'role', 'status', 'salary']

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        username = user_data.get('username')

        organization_data = validated_data.pop('organization')
        org_name = organization_data.get('name')

        user, created = User.objects.get_or_create(username=username)
        organization, created = Organization.objects.get_or_create(name=org_name)
                
        organization_user = UserOrganization.objects.create(user=user, organization=organization, **validated_data)
        return organization_user
        