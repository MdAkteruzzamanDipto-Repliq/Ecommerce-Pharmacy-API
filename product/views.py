from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions as drf_permissions

from core.models import Product, Category
from core import permissions as custom_permissions

from .serializers import ProductSerializer

class CreateProductView(generics.CreateAPIView):
    """
    Create a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [custom_permissions.IsSuperuser, custom_permissions.IsOrganizationInternal]
