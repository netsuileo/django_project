import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from mainapp.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # TODO:

        # 1. Пробежаться по всем категориям в categories.json и записать их в базу
        with open(settings.DATA_ROOT / "categories.json", "r") as file:
            categories = json.load(file)
            for category_data in categories:
                try:
                    category = Category(**category_data)
                    category.save()
                except IntegrityError:
                    pass

        # 2. Пробежаться по всем продуктам в products.json и записать их в базу
        with open(settings.DATA_ROOT / "products.json", "r") as file:
            products = json.load(file)
            for product_data in products:
                product_data["category"] = Category.objects.get(
                    name=product_data["category"]
                )
                product = Product(**product_data)
                product.save()

        # 3: Создать суперпользователя
        User = get_user_model()
        if not User.objects.filter(username="admin"):
            User.objects.create_superuser(username="admin", password="adminadmin")
