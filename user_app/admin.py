from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserRegistrationModel)
class UserRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ("userid","name", "email", "phone",)
    search_fields = ('name', 'phone')


@admin.register(BookDoctorModel)
class BookDoctorModelAdmin(admin.ModelAdmin):
    list_display = ("bookingid","time", "date", "userid", "doctorid")
    fields = ["bookingid","time", "date", "userid", "doctorid"]
    list_filter = ("bookingid","time", "date", "userid", "doctorid")
    
    
@admin.register(ResultsModel)
class ResultsModelAdmin(admin.ModelAdmin):
    list_display = ("resultid", "userid", "doctorid", "testDate", "heartRate", "bloodGroup", "cholesterol", "bloodPressure", "whiteBloodCells", "redBloodCells")
    list_filter = ("resultid", "userid", "doctorid", "testDate")

@admin.register(MedicinesModel)
class MedicinesModelAdmin(admin.ModelAdmin):
    list_display = ("medicineid", "userid", "doctorid", "inferences")
    list_filter = ("medicineid", "userid", "doctorid")

    fieldsets = (
        (None, {
            'fields': ('userid', 'doctorid', 'inferences')
        }),
        ('Medicines 1', {
            'fields': ('med1', 'times1', 'days1')
        }),
        ('Medicines 2', {
            'fields': ('med2', 'times2', 'days2')
        }),
        ('Medicines 3', {
            'fields': ('med3', 'times3', 'days3')
        }),
        ('Medicines 4', {
            'fields': ('med4', 'times4', 'days4')
        }),
        ('Medicines 5', {
            'fields': ('med5', 'times5', 'days5')
        }),
        ('Medicines 6', {
            'fields': ('med6', 'times6', 'days6')
        }),
        ('Medicines 7', {
            'fields': ('med7', 'times7', 'days7')
        }),
        ('Medicines 8', {
            'fields': ('med8', 'times8', 'days8')
        }),
        ('Medicines 9', {
            'fields': ('med9', 'times9', 'days9')
        }),
        ('Medicines 10', {
            'fields': ('med10', 'times10', 'days10')
        }),
    )