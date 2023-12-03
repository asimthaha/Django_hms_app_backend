from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LoginView, name="login"),
    path('displayDoctor/', views.displayDoctorView, name="displayDoctor"),
    path('searchDoctor/', views.searchDoctorView, name='searchDoctor'),
]
