# Generated by Django 5.1.4 on 2025-01-02 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='postal_code',
        ),
    ]