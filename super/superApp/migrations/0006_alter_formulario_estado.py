# Generated by Django 5.0.6 on 2024-07-07 23:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("superApp", "0005_formulario_estado"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulario",
            name="estado",
            field=models.CharField(default="Pendiente", max_length=100),
        ),
    ]