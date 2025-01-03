from rest_framework import serializers

from core.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'manufacturing_date', 'expired_date', 'image', 
                  'availability', 'avg_rating', 'brand', 'status')