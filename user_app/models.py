from django.db import models
from staff_app.models import *

# Create your models here.
class UserRegistration(models.Model):
    """Model definition for UserRegistration."""

    # TODO: Define fields here
    userid = models.AutoField(primary_key=True)
    name=models.CharField(default="",max_length=100)
    email=models.EmailField(default="",max_length=254)
    password=models.CharField(default="",max_length=100)
    phone=models.BigIntegerField(null=True)
    address=models.CharField(default="",max_length=400)

    class Meta:
        """Meta definition for UserRegistration."""

        verbose_name = 'UserRegistration'
        verbose_name_plural = 'UserRegistrations'

    def __str__(self):
        """Unicode representation of UserRegistration."""
        return self.name


class BookDoctorModel(models.Model):
    bookingid = models.AutoField(primary_key=True)
    userid=models.ForeignKey(UserRegistration, null=True, on_delete=models.CASCADE)
    doctorid=models.ForeignKey(DoctorRegistrationModel, null=True, on_delete=models.CASCADE)
    time = models.TimeField()
    date= models.DateField()
    

    class Meta:
        verbose_name = ("BookDoctorModel")
        verbose_name_plural = ("BookDoctorModels")

    def __str__(self):
        return self.time

    def get_absolute_url(self):
        return reverse("BookDoctorModel_detail", kwargs={"pk": self.pk})
