# Generated by Django 5.0 on 2023-12-13 17:10

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="email",
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="origin_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="phonenumbers",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, null=True, region=None
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
