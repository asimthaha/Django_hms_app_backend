from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from user_app.models import *
from user_app.serializer import *
from django.db.models import Q

# Create your views here.
def registerView(request):
    if request.method=="POST":
        data = json.loads(request.body)
        print(data)
        serializer_data = UserRegistrationSerializer(data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"User data Addded Successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"User data - Unsuccessful"}))

def loginView(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        getEmail = data['email']
        getPassword = data['password']
        loginData = UserRegistration.objects.filter(Q(email__exact=getEmail) & Q(password__exact = getPassword)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))
    

def appointDoctorView(request):
    if request.method=="POST":
        data = json.loads(request.body)
        print(data)
        serializer_data = DoctorAppoinmentSerilaizer(data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"Appoinment Successful"}))
        else:
            return HttpResponse(json.dumps({"status":"Appoinment Unsuccessful"}))