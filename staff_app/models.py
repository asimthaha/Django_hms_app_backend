
from django.db import models

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
        ("Oncologist", "Oncologist"),
    )

    doctorid= models.AutoField(primary_key=True)
    name=models.CharField(default="",max_length=100)
    username=models.CharField(default="", max_length=30)
    speciality=models.CharField(default="",
        max_length=100,
        blank=True, 
        null=True,
        choices=SPECIALITY,
        help_text="Speciality")
    startYear=models.IntegerField(null=True)
    password=models.CharField(max_length=50, default="")
    qualification=models.CharField(default="",max_length=100)
    role=models.CharField(default="", max_length=100)

    class Meta:
        verbose_name = ("DoctorRegistrationModel")
        verbose_name_plural = ("DoctorRegistrationModels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DoctorRegistrationModel_detail", kwargs={"pk": self.pk})

