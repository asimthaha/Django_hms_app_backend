# Generated by Django 4.1.13 on 2024-02-29 09:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("staff_app", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserRegistrationModel",
            fields=[
                ("userid", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(db_index=True, default="", max_length=100)),
                ("email", models.EmailField(default="", max_length=254)),
                ("password", models.CharField(default="", max_length=100)),
                ("phone", models.BigIntegerField(null=True)),
            ],
            options={
                "verbose_name": "UserRegistration",
                "verbose_name_plural": "UserRegistrations",
            },
        ),
        migrations.CreateModel(
            name="TransactionModel",
            fields=[
                ("transaction_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "payment_id",
                    models.CharField(max_length=200, verbose_name="Payment Id"),
                ),
                ("order_id", models.CharField(max_length=200, verbose_name="Order Id")),
                (
                    "signature",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Signature"
                    ),
                ),
                ("amount", models.IntegerField(verbose_name="Amount")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="users",
                        to="user_app.userregistrationmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ResultsModel",
            fields=[
                ("resultid", models.AutoField(primary_key=True, serialize=False)),
                ("testDate", models.DateField(blank=True, null=True)),
                (
                    "ecgpwave",
                    models.CharField(
                        blank=True, help_text="81 to 130 ms", max_length=20, null=True
                    ),
                ),
                (
                    "heartRate",
                    models.CharField(
                        blank=True,
                        help_text="Heart Rate eg:60-100 BPM",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "bloodGroup",
                    models.CharField(
                        choices=[
                            ("A+", "A+"),
                            ("A-", "A-"),
                            ("B+", "B+"),
                            ("B-", "B-"),
                            ("AB+", "AB+"),
                            ("AB-", "AB-"),
                            ("O+", "O+"),
                            ("O-", "O-"),
                        ],
                        default="",
                        max_length=20,
                    ),
                ),
                (
                    "bloodPressure",
                    models.CharField(
                        blank=True,
                        help_text="Blood Pressure eg:120/80",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "oxygenSaturation",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="eg:0.95",
                        max_digits=4,
                        null=True,
                    ),
                ),
                (
                    "cholesterol",
                    models.IntegerField(
                        blank=True,
                        help_text="Cholestrol less than 200 mg/dL is normal",
                        null=True,
                    ),
                ),
                (
                    "hdlcholesterol",
                    models.IntegerField(
                        blank=True, help_text="Good Cholestrol eg:60 normal", null=True
                    ),
                ),
                (
                    "ldlcholesterol",
                    models.IntegerField(
                        blank=True,
                        help_text="Bad Cholestrol eg:Under 100 normal",
                        null=True,
                    ),
                ),
                (
                    "cost",
                    models.IntegerField(
                        blank=True, help_text="Cost of checking", null=True
                    ),
                ),
                (
                    "doctorid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctors",
                        to="staff_app.doctorregistrationmodel",
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="user_app.userregistrationmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "ResultsModel",
                "verbose_name_plural": "ResultsModels",
            },
        ),
        migrations.CreateModel(
            name="PredictionModel",
            fields=[
                ("prediction_id", models.AutoField(primary_key=True, serialize=False)),
                ("age", models.FloatField(blank=True, null=True)),
                ("sex", models.FloatField(blank=True, null=True)),
                ("cp", models.FloatField(blank=True, null=True)),
                ("trestbps", models.FloatField(blank=True, null=True)),
                ("chol", models.FloatField(blank=True, null=True)),
                ("fbs", models.FloatField(blank=True, null=True)),
                ("restecg", models.FloatField(blank=True, null=True)),
                ("thalach", models.FloatField(blank=True, null=True)),
                ("exang", models.FloatField(blank=True, null=True)),
                ("oldpeak", models.FloatField(blank=True, null=True)),
                ("slope", models.FloatField(blank=True, null=True)),
                ("ca", models.FloatField(blank=True, null=True)),
                ("thal", models.FloatField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_app.userregistrationmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NotificationsModel",
            fields=[
                (
                    "notification_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("noti_status", models.BooleanField(blank=True, null=True)),
                (
                    "message",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="message for the user",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_app.userregistrationmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicinesModel",
            fields=[
                ("medicineid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "inferences",
                    models.CharField(blank=True, default="", max_length=200, null=True),
                ),
                (
                    "date",
                    models.DateField(default=datetime.date.today, verbose_name="Date"),
                ),
                (
                    "medicines_data",
                    models.JSONField(
                        default=list,
                        help_text='[{"meds":"paracetamol","times":"3 times", "days":"5 days"}]',
                    ),
                ),
                (
                    "total_rate",
                    models.IntegerField(
                        blank=True, help_text="Total Rate of medicine", null=True
                    ),
                ),
                (
                    "doctorid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff_app.doctorregistrationmodel",
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medicines",
                        to="user_app.userregistrationmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "MedicinesModel",
                "verbose_name_plural": "MedicinesModels",
            },
        ),
        migrations.CreateModel(
            name="BookDoctorModel",
            fields=[
                ("bookingid", models.AutoField(primary_key=True, serialize=False)),
                ("time", models.CharField(default="", max_length=20)),
                ("date", models.CharField(default="", max_length=20)),
                (
                    "status",
                    models.CharField(
                        choices=[("Accept", "Accept"), ("Decline", "Decline")],
                        default="",
                        max_length=50,
                    ),
                ),
                (
                    "doctorid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff_app.doctorregistrationmodel",
                    ),
                ),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="user_app.userregistrationmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "BookDoctorModel",
                "verbose_name_plural": "BookDoctorModels",
            },
        ),
        migrations.CreateModel(
            name="BmiModel",
            fields=[
                ("bmi_id", models.AutoField(primary_key=True, serialize=False)),
                ("weight", models.FloatField(blank=True, null=True)),
                ("height", models.FloatField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_app.userregistrationmodel",
                    ),
                ),
            ],
        ),
    ]
