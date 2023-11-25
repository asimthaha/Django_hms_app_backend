from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.loginView, name="Login"),
    path("register/", views.registerView, name="register")
]
