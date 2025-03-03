from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_save, sender=get_user_model())
def user_created(sender, instance, created, **kwargs):
    if created:
        print(f"User {instance.username} has been created.")
