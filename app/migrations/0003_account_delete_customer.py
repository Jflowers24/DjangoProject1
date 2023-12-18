# Generated by Django 5.0 on 2023-12-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_customer_email_customer_origin_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, null=True)),
                ("Phone_Number", models.IntegerField(max_length=20, null=True)),
                ("email", models.EmailField(max_length=50, null=True)),
                ("origin_date", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
    ]
