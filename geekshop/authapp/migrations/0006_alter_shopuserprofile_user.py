# Generated by Django 3.2.11 on 2022-06-03 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0005_shopuserprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuserprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
