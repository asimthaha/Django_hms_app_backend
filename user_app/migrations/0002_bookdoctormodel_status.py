# Generated by Django 4.1.13 on 2024-01-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdoctormodel',
            name='status',
            field=models.CharField(choices=[('Accept', 'Accept'), ('Decline', 'Decline')], default='', max_length=50),
        ),
    ]
