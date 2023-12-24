from django.db import models
from staff_app.models import DoctorRegistrationModel

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
    userid=models.ForeignKey(UserRegistrationModel, null=True, on_delete=models.CASCADE)
    doctorid=models.ForeignKey(DoctorRegistrationModel, null=True, on_delete=models.CASCADE)
    time = models.CharField(max_length=20, default="")
    date= models.CharField(max_length=20, default="")
    

    class Meta:
        verbose_name = ("BookDoctorModel")
        verbose_name_plural = ("BookDoctorModels")


class ResultsModel(models.Model):
    resultid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(UserRegistrationModel, on_delete=models.CASCADE)
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
    rhFactor=models.BooleanField()
    bloodPressure=models.CharField(max_length=20, blank=True,null=True, help_text="Blood Pressure eg:120/80")
    oxygenSaturation=models.DecimalField(max_digits=4, decimal_places=2, blank=True,null=True, help_text="eg:0.95")
    cholesterol=models.IntegerField(blank=True,null=True, help_text="Cholestrol less than 200 mg/dL is normal")
    hdlcholesterol=models.IntegerField(blank=True,null=True, help_text="Good Cholestrol eg:60 normal")
    ldlcholesterol=models.IntegerField(blank=True,null=True, help_text="Bad Cholestrol eg:Under 100 normal")
    uricAcid=models.FloatField(blank=True,null=True, help_text="2.5 - 7.0 milligrams per deciliter (mg/dL)")
    serumLeucocytes=models.IntegerField(blank=True,null=True, help_text="leukocytes (adults and children >2 years) - 5000-10,000/mm")
    whiteBloodCells=models.IntegerField(blank=True,null=True, help_text="WBCs in the blood is 4,500 to 11,000 WBCs per microliter")
    redBloodCells=models.IntegerField(blank=True,null=True, help_text="RBC 4.35 to 5.65 (mcL)")
    
    class Meta:
        verbose_name = ("ResultsModel")
        verbose_name_plural = ("ResultsModels")
    def __str__(self):
        return f'{self.resultid} - {self.doctorid} - {self.testDate} - {self.userid}'
        