from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.loginView, name="Login"),
    path("register/", views.registerView, name="register"),
    #path('logout',views.logout_view),
    path('bmiCalc/', views.bmiCalculatorView, name='bmiCalc'),
    path('bookDoctor/', views.appointDoctorView, name='bookDoctor'),
    
]
