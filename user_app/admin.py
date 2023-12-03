from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserRegistration)
class UserRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ("userid","name", "email", "phone", "address")
    search_fields = ('name', 'phone')


@admin.register(BookDoctorModel)
class BookDoctorModelAdmin(admin.ModelAdmin):
    list_display = ("time", "date")
    fields = ["time", "date"]
    list_filter = ("time", "date")