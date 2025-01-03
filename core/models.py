from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from autoslug import AutoSlugField
from versatileimagefield.fields import VersatileImageField

from phonenumber_field.modelfields import PhoneNumberField

import uuid

from .managers import UserManager
from .choices import GenderChoices, StatusChoices, RoleChoices, ProductStockChoices, ProductStatusChoices

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.CHOICES, blank=True)
    address = models.CharField(max_length=255, blank=True)
    thana = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postal_code = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True)
    image = VersatileImageField('Image', upload_to='images/user/', blank=True,)
    status = models.CharField(max_length=10, choices=StatusChoices.CHOICES, default=StatusChoices.Active)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(populate_from = 'username', unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email

class Organization(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = PhoneNumberField(blank=True)
    trade_license = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    thana = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postal_code = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True)
    logo = VersatileImageField('Image', upload_to='images/organization/', blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length = 10, choices=StatusChoices.CHOICES, default=StatusChoices.Active)
    slug = AutoSlugField(populate_from = 'name', unique=True)
    
    REQUIRED_FIELDS = ['name', 'email', 'trade_license']
    
    def __str__(self):
        return self.name
    
class UserOrganization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(choices=RoleChoices.CHOICES, blank=True)
    status = models.CharField(choices=StatusChoices.CHOICES, default=StatusChoices.Active)
    date_joined = models.DateField(default=timezone.now)
    salary = models.FloatField()
    # slug = AutoSlugField(populate_from = 'user.name')
    
        
    def __str__(self):
        return self.user.username +  " " + self.organization.name +  " " + self.role
    
def generate_slug(instance):
    return f"{instance.name}-{instance.location}".lower()

class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    manufacturing_date = models.DateField()
    expired_date = models.DateField()
    price = models.FloatField()
    image = VersatileImageField('Image', upload_to='images/product/', blank=True)
    availability = models.CharField(max_length=20, choices=ProductStockChoices.CHOICES, default=ProductStockChoices.InStock)
    avg_rating = models.FloatField(blank=True)
    brand = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=ProductStatusChoices.CHOICES, default=ProductStatusChoices.Published)
    slug = AutoSlugField(
        populate_from=generate_slug,
        unique=True
    )

    def __str__(self):
        return self.name
    
class Category(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    
    def __str__(self):
        return self.name
