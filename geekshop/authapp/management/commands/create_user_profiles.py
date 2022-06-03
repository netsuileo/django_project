from authapp.models import ShopUser, ShopUserProfile
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = ShopUser.objects.all()
        for user in users:
            profile = ShopUserProfile.objects.filter(user=user).first()
            if not profile:
                profile = ShopUserProfile(user=user)
                profile.save()
