from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from user_app.models import *
from user_app.serializer import *
from staff_app.models import *
from staff_app.serializer import *
from django.db.models import Q


# Create your views here.
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        getUsername = data['username']
        getPassword = data['password']
        loginData = DoctorRegistrationModel.objects.filter(
            Q(username__exact=getUsername) & Q(password__exact=getPassword)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))


@csrf_exempt
def display_doctor_view(request):
    if request.method == "POST":
        data = DoctorRegistrationModel.objects.filter(role="Doctor").all()
        serializer_data = DoctorSerializer(data, many=True)
        return HttpResponse(json.dumps(serializer_data.data))


@csrf_exempt
def search_doctor_view(request):
    if request.method == "POST":
        received_data = json.loads(request.body)
        getSpecilality = received_data['speciality']
        data = DoctorRegistrationModel.objects.filter(Q(speciality__icontains=getSpecilality)).values()
        searchDoctorData = list(data)
        return HttpResponse(json.dumps(searchDoctorData))


@csrf_exempt
def search_patient_view(request):
    if request.method == "POST":
        received_data = json.loads(request.body)
        getName = received_data['name']
        data = UserRegistrationModel.objects.filter(Q(name__icontains=getName)).prefetch_related('results', 'medicines', 'bookings').all()
        serializer_data = searchPatientDataSerializer(data, many=True)
        return JsonResponse(serializer_data.data, safe=False)

@csrf_exempt
def appoinment_view(request):
    if request.method == "POST":
        received_data = json.loads(request.body)
        get_doctor_id = received_data["doctorid"]
        data = BookDoctorModel.objects.filter(Q(doctorid__exact=get_doctor_id)).all()
        serializer_data = BookingSerializer(data, many=True)
        return HttpResponse(json.dumps(serializer_data.data))

@csrf_exempt
def appoinment_decline_view(request):
    if request.method == "DELETE":
        received_data = json.loads(request.body)
        getBookingid = received_data['doctorid']
        if getBookingid is not None:
            try:
                data = BookDoctorModel.objects.filter(Q(bookingid__exact=getBookingid))   
            except BookDoctorModel.DoesNotExist:
                return HttpResponse(json.dumps({"status":"User not Found"}))  
            data.delete()
            return HttpResponse(json.dumps({"status":" Appoinment Deleted Successfully"}))
        

@csrf_exempt
def add_medicine_view(request):
    if request.method=="POST":
        data = json.loads(request.body)
        serializer_data = MedicineSerializer(data=data)
        print(serializer_data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"Medicine data Added Successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"Medicine data - Unsuccessful"}))
        
@csrf_exempt
def view_medicine_pharamacist_view(request):
    if request.method=="POST":
        data = MedicinesModel.objects.all()
        serializer_data = MedicineSerializerForViewing(data, many=True)
        return HttpResponse(json.dumps(serializer_data.data))