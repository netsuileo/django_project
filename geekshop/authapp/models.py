from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    city = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to="user_images", blank=True)
