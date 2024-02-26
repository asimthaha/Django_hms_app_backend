# Register your models here.
from django.contrib import admin
from .models import *
from user_app.models import *



# Register your models here.
@admin.register(DoctorRegistrationModel)
class DoctorRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ('staffid', 'name', 'username', 'role', 'startYear', 'password', 'qualification')
    list_filter = ('name', 'username', 'role', 'qualification')
    search_fields = ('name', 'username', 'role', 'qualification', 'startYear')


# @admin.register(TaxSlabRates)
# class TaxSlabRatesAdmin(admin.ModelAdmin):
#     list_display = ("regime", "slabs", "rates", "age_group")
#     list_filter = ("regime", "age_group")


# @admin.register(TaxSavingsGuide)
# class TaxSavingsGuideAdmin(admin.ModelAdmin):
#     list_display = ("photo", "card_title", "card_description")
#     fields = ["photo", "card_title", "card_description"]
#     list_filter = ("card_title", "photo")
    
@admin.register(NotificationsModel)
class NotificationsModelAdmin(admin.ModelAdmin):
    list_display = ('notification_id', 'user_id', 'noti_status', 'message')
    list_filter = ('notification_id', 'noti_status')
    search_fields = ('notification_id', 'noti_status', 'user_id')