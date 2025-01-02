from rest_framework import serializers

from core.models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'email', 'phone', 'trade_license', 'address', 'thana', 'city', 'postal_code', 
                  'country', 'logo', 'description', 'status']
        
    def __init__(self, *args, **kwargs):
        exclude = kwargs.pop('exclude', None)
        super().__init__(*args, **kwargs)
        if exclude:
            for field in exclude:
                self.fields.pop(field, None)
        