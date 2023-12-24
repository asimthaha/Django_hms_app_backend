from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserRegistrationModel)
class UserRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ("userid","name", "email", "phone",)
    search_fields = ('name', 'phone')


@admin.register(BookDoctorModel)
class BookDoctorModelAdmin(admin.ModelAdmin):
    list_display = ("time", "date", "userid", "doctorid")
    fields = ["time", "date", "userid", "doctorid"]
    list_filter = ("time", "date", "userid", "doctorid")
    
    
@admin.register(ResultsModel)
class ResultsModelAdmin(admin.ModelAdmin):
    list_display = ("resultid", "userid", "doctorid", "testDate", "heartRate", "bloodGroup", "cholesterol", "bloodPressure", "whiteBloodCells", "redBloodCells")
    list_filter = ("resultid", "userid", "doctorid", "testDate")