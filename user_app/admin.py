from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserRegistrationModel)
class UserRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ("userid","name", "email", "phone",)
    search_fields = ('name', 'phone')


@admin.register(BookDoctorModel)
class BookDoctorModelAdmin(admin.ModelAdmin):
    list_display = ("bookingid","time", "date", "userid", "doctorid","status")
    fields = ["time", "date", "userid", "doctorid"]
    list_filter = ("bookingid","time", "date", "userid", "doctorid")
    
    
@admin.register(ResultsModel)
class ResultsModelAdmin(admin.ModelAdmin):
    list_display = ("resultid", "userid", "doctorid", "testDate", "heartRate", "bloodGroup", "cholesterol", "bloodPressure","cost")
    list_filter = ("resultid", "userid", "doctorid", "testDate")

@admin.register(MedicinesModel)
class MedicinesModelAdmin(admin.ModelAdmin):
    list_display = ("medicineid", "userid", "doctorid", "inferences", 'date', 'total_rate')
    list_filter = ("medicineid", "userid", "doctorid")

    fieldsets = (
    (None, {
        'fields': ('userid', 'doctorid', 'inferences', 'date')
    }),
    ('Medicines', {
        'fields': ('medicines_data',)  # Note the comma at the end to make it a tuple
    }),
)


@admin.register(TransactionModel)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ("transaction_id", "user_id", "payment_id", "order_id", "signature", "amount", 'created_at')
    list_filter = ("amount", "user_id", "created_at")


@admin.register(PredictionModel)
class PredictionModelAdmin(admin.ModelAdmin):
    list_display = ("prediction_id", "user_id", "age", "sex", "cp", "trestbps", "fbs", "restecg","thalach", "created_at")
    search_fields = ('prediction_id', 'age')

@admin.register(BmiModel)
class BmiModelAdmin(admin.ModelAdmin):
    list_display = ("bmi_id", "user_id", "weight", "height", "created_at")
    search_fields = ('bmi_id', 'user_id')