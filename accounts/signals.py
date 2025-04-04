from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser

@receiver(post_migrate)
def create_roles(sender, **kwargs):
    if sender.name == "accounts":
        roles = ['Admin', 'Creator', 'Customer']
        for role in roles:
            Group.objects.get_or_create(name=role)
