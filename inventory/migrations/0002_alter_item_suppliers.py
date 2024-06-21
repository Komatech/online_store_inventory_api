# Generated by Django 5.0.6 on 2024-06-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="suppliers",
            field=models.ManyToManyField(
                blank=True, related_name="items", to="inventory.supplier"
            ),
        ),
    ]
