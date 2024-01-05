from django.db import models
from staff_app.models import DoctorRegistrationModel
import datetime

# Create your models here.
class UserRegistrationModel(models.Model):
    """Model definition for UserRegistration."""

    # TODO: Define fields here
    userid = models.AutoField(primary_key=True)
    name=models.CharField(default="",max_length=100, db_index=True)
    email=models.EmailField(default="",max_length=254)
    password=models.CharField(default="",max_length=100)
    phone=models.BigIntegerField(null=True)

    class Meta:
        """Meta definition for UserRegistration."""

        verbose_name = 'UserRegistration'
        verbose_name_plural = 'UserRegistrations'

    def __str__(self):
        """Unicode representation of UserRegistration."""
        return self.name


class BookDoctorModel(models.Model):
    bookingid = models.AutoField(primary_key=True)
    userid=models.ForeignKey(UserRegistrationModel, related_name='bookings', null=True, on_delete=models.CASCADE)
    doctorid=models.ForeignKey(DoctorRegistrationModel, null=True, on_delete=models.CASCADE)
    time = models.CharField(max_length=20, default="")
    date= models.CharField(max_length=20, default="")
    

    class Meta:
        verbose_name = ("BookDoctorModel")
        verbose_name_plural = ("BookDoctorModels")


class ResultsModel(models.Model):
    resultid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(UserRegistrationModel, related_name='results', on_delete=models.CASCADE)
    doctorid=models.ForeignKey(DoctorRegistrationModel, on_delete=models.CASCADE)
    testDate=models.DateField(blank= True, null=True)
    
    ecgpwave = models.CharField(max_length=20, blank=True,null=True, help_text="81 to 130 ms")
    heartRate=models.CharField(max_length=20, blank=True,null=True, help_text="Heart Rate eg:60-100 BPM")
    
    BLOOD_GROUP = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    )
    bloodGroup=models.CharField(max_length=20,
                                default="",
                                choices=BLOOD_GROUP)
    bloodPressure=models.CharField(max_length=20, blank=True,null=True, help_text="Blood Pressure eg:120/80")
    oxygenSaturation=models.DecimalField(max_digits=4, decimal_places=2, blank=True,null=True, help_text="eg:0.95")
    cholesterol=models.IntegerField(blank=True,null=True, help_text="Cholestrol less than 200 mg/dL is normal")
    hdlcholesterol=models.IntegerField(blank=True,null=True, help_text="Good Cholestrol eg:60 normal")
    ldlcholesterol=models.IntegerField(blank=True,null=True, help_text="Bad Cholestrol eg:Under 100 normal")
    # uricAcid=models.FloatField(blank=True,null=True, help_text="2.5 - 7.0 milligrams per deciliter (mg/dL)")
    # serumLeucocytes=models.IntegerField(blank=True,null=True, help_text="leukocytes (adults and children >2 years) - 5000-10,000/mm")
    # whiteBloodCells=models.IntegerField(blank=True,null=True, help_text="WBCs in the blood is 4,500 to 11,000 WBCs per microliter")
    # redBloodCells=models.IntegerField(blank=True,null=True, help_text="RBC 4.35 to 5.65 (mcL)")
    
    class Meta:
        verbose_name = ("ResultsModel")
        verbose_name_plural = ("ResultsModels")
    def __str__(self):
        return f'{self.resultid} - {self.doctorid} - {self.testDate} - {self.userid}'


class MedicinesModel(models.Model):

    medicineid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(UserRegistrationModel, related_name='medicines', on_delete=models.CASCADE)
    doctorid=models.ForeignKey(DoctorRegistrationModel, on_delete=models.CASCADE)
    inferences = models.CharField(max_length=200, default="", blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.date.today)

    med1 = models.CharField(max_length=50, default="", blank=True, null=True)
    times1 = models.CharField(max_length=20, default="", blank=True, null=True)
    days1 = models.CharField(max_length=20, default="", blank=True, null=True)
    med2 = models.CharField(max_length=50, default="", blank=True, null=True)
    times2 = models.CharField(max_length=20, default="", blank=True, null=True)
    days2 = models.CharField(max_length=20, default="", blank=True, null=True)

    # med3 = models.CharField(max_length=50, default="", blank=True, null=True)
    # times3 = models.CharField(max_length=20, default="", blank=True, null=True)
    # days3 = models.CharField(max_length=20, default="", blank=True, null=True)
    # med4 = models.CharField(max_length=50, default="", blank=True, null=True)
    # times4 = models.CharField(max_length=20, default="", blank=True, null=True)
    # days4 = models.CharField(max_length=20, default="", blank=True, null=True)

    # med5 = models.CharField(max_length=50, default="", blank=True, null=True)
    # times5 = models.CharField(max_length=20, default="", blank=True, null=True)
    # days5 = models.CharField(max_length=20, default="", blank=True, null=True)
    # med6 = models.CharField(max_length=50, default="", blank=True, null=True)
    # times6 = models.CharField(max_length=20, default="", blank=True, null=True)
    # days6 = models.CharField(max_length=20, default="", blank=True, null=True)

    # med7 = models.CharField(max_length=50, default="", blank=True, null=True)
    # times7 = models.CharField(max_length=20, default="", blank=True, null=True)
    # days7 = models.CharField(max_length=20, default="", blank=True, null=True)
    # med8 = models.CharField(max_length=50, default="", blank=True, null=True)
    # times8 = models.CharField(max_length=20, default="", blank=True, null=True)
    # days8 = models.CharField(max_length=20, default="", blank=True, null=True)

    # med9 = models.CharField(max_length=50, default="", blank=True, null=True)
    # times9 = models.CharField(max_length=20, default="", blank=True, null=True)
    # days9 = models.CharField(max_length=20, default="", blank=True, null=True)
    # med10 = models.CharField(max_length=50, default="", blank=True, null=True)
    # times10 = models.CharField(max_length=20, default="", blank=True, null=True)
    # days10 = models.CharField(max_length=20, default="", blank=True, null=True)

    class Meta:
        """Meta definition for MedicinesModel."""

        verbose_name = 'MedicinesModel'
        verbose_name_plural = 'MedicinesModels'