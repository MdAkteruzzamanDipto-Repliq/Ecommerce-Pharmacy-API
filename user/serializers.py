from django.contrib.auth import authenticate

from rest_framework import serializers

from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone', 'gender', 'address', 'thana', 'city', 
                  'postal_code', 'country', 'image', 'status', 'is_active', 'is_staff', 'date_joined', 'slug']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }
        read_only_fields = ('is_staff', 'is_superuser')
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save()
        
        return user
    
    
    
# class SuperuserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'first_name', 'last_name']
        