# Generated by Django 4.2.2 on 2024-02-25 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0004_room_category_alter_room_amenities_alter_room_owner"),
        ("experiences", "0004_alter_perk_details"),
        ("medias", "0005_alter_photo_experience_alter_photo_room"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="experiences.experience",
            ),
        ),
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="rooms.room",
            ),
        ),
    ]
