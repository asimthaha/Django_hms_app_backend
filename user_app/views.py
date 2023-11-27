from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from user_app.models import *
from user_app.serializer import *
from django.db.models import Q

# Create your views here.
@csrf_exempt
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

@csrf_exempt
def loginView(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        getEmail = data['email']
        getPassword = data['password']
        loginData = UserRegistration.objects.filter(Q(email__exact=getEmail) & Q(password__exact = getPassword)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))
    
@csrf_exempt
def displayUserDataView(request):
    if request.method =="POST":
        recieved_data = json.loads(request.body)
        getUserid = recieved_data["userid"]
        data = UserRegistration.objects.filter(Q(userid__exact=getUserid)).values()
        data = list(data)
        return HttpResponse(json.dumps(data))
    
@csrf_exempt
def updateUserDataView(request):
    if request.method == "PUT":      
        recieved_data = json.loads(request.body)
        getUserid = recieved_data["userid"]
        getName = recieved_data["name"]
        getEmail = recieved_data["email"]
        getPhone = recieved_data["phone"]
        getPassword = recieved_data["password"]
        getAddress = recieved_data["address"]
        data = UserRegistration.objects.filter(Q(userid__exact=getUserid))
        data.update(name=getName,email= getEmail,phone=getPhone,password= getPassword, address=getAddress)
        return HttpResponse(json.dumps({"status":"Data Updated Successfully"}))

@csrf_exempt        
def bmiCalculatorView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        getWeight = data['weight']
        getHeight = data['height']
        bmi = getWeight/((getHeight/100)**2)
        return HttpResponse(json.dumps(bmi))
    
@csrf_exempt
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

@csrf_exempt
def searchDoctorView(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        getSpecilality = recieved_data['speciality']
        data = DoctorModel.objects.filter(Q(speciality__icontains=getSpecilality)).values()
        searchData= list(data)
        return HttpResponse(json.dumps(searchData))