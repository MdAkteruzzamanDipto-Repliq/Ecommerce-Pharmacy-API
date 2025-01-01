from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from autoslug import AutoSlugField
from versatileimagefield.fields import VersatileImageField

import uuid

from .managers import UserManager
from .choices import GenderChoices, UserStatusChoices

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.CHOICES, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    thana = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    image = VersatileImageField('Image', upload_to='images/core/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=UserStatusChoices.CHOICES, default=UserStatusChoices.Active)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(populate_from = 'username')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email

