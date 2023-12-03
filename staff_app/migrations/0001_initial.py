# Generated by Django 4.1.13 on 2023-11-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorRegistrationModel',
            fields=[
                ('doctorid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('username', models.CharField(default='', max_length=30)),
                ('speciality', models.CharField(blank=True, choices=[('Dentist', 'Dentist'), ('Gynecologist', 'Gynecologist'), ('Genaral Physician', 'Genaral Physician'), ('Dermatologist', 'Dermatologist'), ('ENT specialist', 'ENT specialist'), ('Nephrologist', 'Nephrologist'), ('Cardiologist', 'Cardiologist'), ('Oncologist', 'Oncologist')], default='', help_text='Speciality', max_length=100, null=True)),
                ('startYear', models.IntegerField(null=True)),
                ('password', models.CharField(default='', max_length=50)),
                ('qualification', models.CharField(default='', max_length=100)),
                ('role', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'DoctorRegistrationModel',
                'verbose_name_plural': 'DoctorRegistrationModels',
            },
        ),
    ]
