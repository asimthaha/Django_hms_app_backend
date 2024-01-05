# Generated by Django 4.1.13 on 2024-01-05 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_alter_medicinesmodel_userid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='days10',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='days3',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='days4',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='days5',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='days6',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='days7',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='days8',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='days9',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='med10',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='med3',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='med4',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='med5',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='med6',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='med7',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='med8',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='med9',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='times10',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='times3',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='times4',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='times5',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='times6',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='times7',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='times8',
        ),
        migrations.RemoveField(
            model_name='medicinesmodel',
            name='times9',
        ),
        migrations.AddField(
            model_name='medicinesmodel',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
