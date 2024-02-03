from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login_view, name="Login"),
    path("register/", views.register_view, name="register"),
    path('displayUserData', views.display_userdata_view, name="displayUserData"),
    path('updateUserData', views.update_userdata_view, name="updateUserData"),
    path('bmiCalc/', views.bmi_calculator_view, name='bmiCalc'), 
    path('predictHeart/', views.predict_heart_view, name='predictHeart'),
    path('bookDoctor/', views.appoint_doctor_view, name='bookDoctor'),
    path('disableAppoinments/', views.disable_appoinments_View, name='disableAppoinments'),
    path('viewResultsUser/', views.view_results_user_view, name='viewResultsUser'),
    path('viewMedicinesUser/', views.view_medicine_user_view, name='viewMedicinesUser'),
    path("payment/create/", views.create_order_view, name="razorpay-create-order-api"),
    path("payment/complete/", views.verify_payment_view, name="razorpay-complete-order-api"),
]
