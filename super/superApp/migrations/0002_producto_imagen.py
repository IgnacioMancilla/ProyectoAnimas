# Generated by Django 5.0.6 on 2024-06-25 03:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("superApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="imagen",
            field=models.ImageField(default="", upload_to=""),
        ),
    ]
