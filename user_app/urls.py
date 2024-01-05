from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.loginView, name="Login"),
    path("register/", views.registerView, name="register"),
    # path('logout',views.logout_view),
    path('displayUserData', views.displayUserDataView, name="displayUserData"),
    path('updateUserData', views.updateUserDataView, name="updateUserData"),
    path('bmiCalc/', views.bmiCalculatorView, name='bmiCalc'), 
    path('predictHeart/', views.predictHeartView, name='predictHeart'),
    path('bookDoctor/', views.appointDoctorView, name='bookDoctor'),
]
