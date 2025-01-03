# Generated by Django 5.1.4 on 2025-01-03 08:25

import autoslug.fields
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import uuid
import versatileimagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('trade_license', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('thana', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('logo', versatileimagefield.fields.VersatileImageField(blank=True, upload_to='images/organization/', verbose_name='Image')),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('removed', 'Removed')], default='active', max_length=10)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('thana', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, upload_to='images/user/', verbose_name='Image')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('removed', 'Removed')], default='active', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='username', unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('owner', 'Owner'), ('admin', 'Admin'), ('manager', 'Manager'), ('staff', 'Staff')])),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('removed', 'Removed')], default='active')),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('salary', models.FloatField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
