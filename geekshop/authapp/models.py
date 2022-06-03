import uuid
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


def get_activation_key_expires():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    city = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to="user_images", blank=True)

    activation_key = models.UUIDField(default=uuid.uuid4)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)

    @property
    def is_activation_key_expired(self):
        return now() > self.activation_key_expires

    def activate(self):
        self.is_active = True
        self.activation_key_expires = now()


class ShopUserProfile(models.Model):
    MALE = "M"
    FEMALE = "F"
    NON_BINARY = "N"

    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (NON_BINARY, "Non Binary"),
    ]

    user = models.OneToOneField(
        ShopUser, related_name="profile", on_delete=models.CASCADE
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    about = models.TextField(blank=True)

    @receiver(post_save, sender=ShopUser)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            profile = ShopUserProfile(user=instance)
            profile.save()
