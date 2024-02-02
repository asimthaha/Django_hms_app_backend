from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('displayDoctor/', views.display_doctor_view, name="displayDoctor"),
    path('searchDoctor/', views.search_doctor_view, name='searchDoctor'),
    path('searchPatient/', views.search_patient_view, name='searchPatient'),
    path('appoinmentViewDoctor/', views.appoinment_view, name='appoinmentViewDoctor'),
    path('appoinmentStatusUpdateDoctor/', views.appoinment_status_update_view, name='appoinmentStatusUpdateDoctor'),
    path('appoinmentDeclineDoctor/', views.appoinment_decline_view, name='appoinmentDeclineDoctor'),
    path('addMedicineDoctor/', views.add_medicine_view, name='addMedicineDoctor'),
    path('viewMedicinePharmacist/', views.view_medicine_pharamacist_view, name='viewMedicinePharmacist'),
    path('updateMedicinePharmacist/', views.update_medicine_pharamacist_view, name='updateMedicinePharmacist'),
]
