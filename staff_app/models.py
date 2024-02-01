
from django.db import models
from django.urls import reverse 

# Create your models here.
class DoctorRegistrationModel(models.Model):
    
    SPECIALITY = (
        ("Dentist", "Dentist"),
        ("Gynecologist", "Gynecologist"),
        ("Genaral Physician", "Genaral Physician"),
        ("Dermatologist", "Dermatologist"),
        ("ENT specialist", "ENT specialist"),
        ("Nephrologist", "Nephrologist"),
        ("Cardiologist", "Cardiologist"),
    )

    staffid= models.AutoField(primary_key=True)
    name=models.CharField(default="",max_length=100, db_index=True)
    photo = models.ImageField(upload_to="photo", blank=True, null=True)
    username=models.CharField(default="", max_length=30)
    speciality=models.CharField(default="Cardiologist",
        max_length=100,
        blank=True, 
        null=True,
        choices=SPECIALITY)
    startYear=models.IntegerField(null=True)
    password=models.CharField(max_length=50, default="")
    qualification=models.CharField(default="",max_length=100, db_index=True)
    
    ROLE = (
        ("Doctor", "Doctor"),
        ("Pharmacist", "Pharmacist"),
        ("LabAssistant", "LabAssistant"),
    )
    role=models.CharField(default="",
                          blank=True,
                          null=True,
                          choices=ROLE,
                          max_length=100)

    class Meta:
        verbose_name = ("DoctorRegistrationModel")
        verbose_name_plural = ("DoctorRegistrationModels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DoctorRegistrationModel_detail", kwargs={"pk": self.pk})

# class MedicineDetailsModel(models.Model):
