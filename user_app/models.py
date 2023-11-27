from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    """Model definition for UserRegistration."""

    # TODO: Define fields here
    userid = models.AutoField(primary_key=True,)
    name=models.CharField(default="",max_length=100)
    email=models.EmailField(default="",max_length=254)
    password=models.CharField(default="",max_length=100)
    phone=models.IntegerField(null=True)
    address=models.CharField(default="",max_length=400)
    



    class Meta:
        """Meta definition for UserRegistration."""

        verbose_name = 'UserRegistration'
        verbose_name_plural = 'UserRegistrations'

    def __str__(self):
        """Unicode representation of UserRegistration."""
        pass


class BookDoctorModel(models.Model):

    time = models.TimeField()
    date= models.DateField()
    

    class Meta:
        verbose_name = ("BookDoctorModel")
        verbose_name_plural = ("BookDoctorModels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BookDoctorModel_detail", kwargs={"pk": self.pk})
