from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from staff_app.models import *
from staff_app.serializer import *
from django.db.models import Q



# Create your views here.
@csrf_exempt
def LoginView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        getUsername = data['username']
        getPassword = data['password']
        loginData = DoctorRegistrationModel.objects.filter(
            Q(username__exact=getUsername) & Q(password__exact=getPassword)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))


@csrf_exempt
def displayDoctorView(request):
    if request.method == "POST":
        data = DoctorRegistrationModel.objects.all()
        serializer_data = DoctorSerializer(data, many=True)
        return HttpResponse(json.dumps(serializer_data.data))


@csrf_exempt
def searchDoctorView(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        getSpecilality = recieved_data['speciality']
        data = DoctorRegistrationModel.objects.filter(Q(speciality__icontains=getSpecilality)).values()
        searchData = list(data)
        return HttpResponse(json.dumps(searchData))



