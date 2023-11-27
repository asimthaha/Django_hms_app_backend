# Generated by Django 4.1.13 on 2023-11-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDoctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'BookDoctorModel',
                'verbose_name_plural': 'BookDoctorModels',
            },
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('password', models.CharField(default='', max_length=100)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.CharField(default='', max_length=400)),
            ],
            options={
                'verbose_name': 'UserRegistration',
                'verbose_name_plural': 'UserRegistrations',
            },
        ),
    ]
