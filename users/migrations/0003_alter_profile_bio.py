# Generated by Django 5.0.2 on 2024-09-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_profile_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]