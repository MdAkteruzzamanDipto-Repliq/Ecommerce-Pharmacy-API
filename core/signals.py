from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, Organization, UserOrganization

@receiver(post_save, sender=User)
def update_userorganization_status_based_on_user_status(sender, instance, **kwargs):
    user_status = instance.status
    UserOrganization.objects.filter(user=instance).update(status = user_status)
    
@receiver(post_save, sender=Organization)
def update_userorganization_status_based_on_organization_status(sender, instance, **kwargs):
    organization_status = instance.status
    UserOrganization.objects.filter(organization=instance).update(status = organization_status)