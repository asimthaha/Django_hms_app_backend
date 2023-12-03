# Register your models here.
from django.contrib import admin
from .models import *



# Register your models here.
@admin.register(DoctorRegistrationModel)
class DoctorRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ('doctorid', 'name', 'username', 'speciality', 'startYear', 'password', 'qualification')
    list_filter = ('name', 'username', 'speciality', 'qualification')
    search_fields = ('name', 'username', 'speciality', 'qualification', 'startYear')


# @admin.register(TaxSlabRates)
# class TaxSlabRatesAdmin(admin.ModelAdmin):
#     list_display = ("regime", "slabs", "rates", "age_group")
#     list_filter = ("regime", "age_group")


# @admin.register(TaxSavingsGuide)
# class TaxSavingsGuideAdmin(admin.ModelAdmin):
#     list_display = ("photo", "card_title", "card_description")
#     fields = ["photo", "card_title", "card_description"]
#     list_filter = ("card_title", "photo")