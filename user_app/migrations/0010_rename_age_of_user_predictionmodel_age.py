# Generated by Django 4.1.13 on 2024-02-27 06:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0009_rename_notification_id_bmimodel_bmi_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="predictionmodel",
            old_name="age_of_user",
            new_name="age",
        ),
    ]
