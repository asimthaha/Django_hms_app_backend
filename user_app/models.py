from django.db import models
from staff_app.models import DoctorRegistrationModel
import datetime
from django.db.models import JSONField

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
    STATUS= (
        ('Accept','Accept'),
        ('Decline','Decline'),
    )
    status=models.CharField(max_length=50, default="", choices=STATUS)
    

    class Meta:
        verbose_name = ("BookDoctorModel")
        verbose_name_plural = ("BookDoctorModels")


class ResultsModel(models.Model):
    resultid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(UserRegistrationModel, related_name='results', on_delete=models.CASCADE)
    doctorid=models.ForeignKey(DoctorRegistrationModel, related_name='doctors', on_delete=models.CASCADE)
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
    medicines_data = models.JSONField(default=list, help_text='[{"meds":"paracetamol","times":"3 times", "days":"5 days"}]')
    STATUS= (
        ('Accept','Accept'),
        ('Decline','Decline'),
    )
    med_status=models.CharField(max_length=50, default="", choices=STATUS)
    total_rate=models.IntegerField(blank=True,null=True, help_text="Total Rate of medicine")

    class Meta:
        """Meta definition for MedicinesModel."""

        verbose_name = 'MedicinesModel'
        verbose_name_plural = 'MedicinesModels'


class TransactionModel(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserRegistrationModel, on_delete=models.CASCADE, related_name='users')
    payment_id=models.CharField(max_length=200, verbose_name="Payment Id")
    order_id = models.CharField(max_length=200, verbose_name="Order Id")
    signature = models.CharField(max_length=500, verbose_name="Signature", blank=True, null=True)
    amount = models.IntegerField(verbose_name="Amount")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


