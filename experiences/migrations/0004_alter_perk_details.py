# Generated by Django 4.2.2 on 2024-01-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "experiences",
            "0003_alter_experience_category_alter_experience_host_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="perk",
            name="details",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
    ]
