# Generated by Django 4.1.13 on 2024-02-27 06:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "user_app",
            "0008_rename_notification_id_predictionmodel_prediction_id_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="bmimodel",
            old_name="notification_id",
            new_name="bmi_id",
        ),
    ]