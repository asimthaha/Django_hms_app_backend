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
from datetime import datetime


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


def convert_datetime(data):
    date_str = data['date']
    time_str = data['time']
    datetime_str = f"{date_str} {time_str}"
    return datetime.strptime(datetime_str, "%d/%m/%Y %I:%M %p")

@csrf_exempt
def appoinment_view(request):
    if request.method == "POST":
        received_data = json.loads(request.body)
        get_doctor_id = received_data["doctorid"]
        data = BookDoctorModel.objects.filter(Q(doctorid__exact=get_doctor_id)).all()
        serializer_data = BookingViewSerializer(data, many=True)
        sorted_data = sorted(serializer_data.data, key=convert_datetime)
        return HttpResponse(json.dumps(sorted_data))
    
@csrf_exempt
def appoinment_status_update_view(request):
    if request.method == "PUT":
        received_data = json.loads(request.body)
        get_booking_id = received_data["bookingid"]
        get_status = received_data["status"]
        data = BookDoctorModel.objects.filter(Q(bookingid__exact=get_booking_id)).update(status=get_status)
        return HttpResponse(json.dumps({"status":"Updation successful"}))
    else:
        return HttpResponse(json.dumps({"status":"updation unsuccessful"}))

@csrf_exempt
def appoinment_decline_view(request):
    if request.method == "DELETE":
        received_data = json.loads(request.body)
        getBookingid = received_data['doctorid']
        if getBookingid is not None:
            try:
                data = BookDoctorModel.objects.filter(Q(bookingid__exact=getBookingid))   
            except BookDoctorModel.DoesNotExist:
                return HttpResponse(json.dumps({"status":"User not found"}))  
            data.delete()
            return HttpResponse(json.dumps({"status":" Appoinment deleted successfully"}))
        

@csrf_exempt
def add_medicine_view(request):
    if request.method=="POST":
        data = json.loads(request.body)
        serializer_data = MedicineSerializer(data=data)
        print(serializer_data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"Medicine data added successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"Medicine data unsuccessful"}))
        
@csrf_exempt
def view_medicine_pharamacist_view(request):
    if request.method=="POST":
        data = MedicinesModel.objects.all().order_by('date')
        serializer_data = MedicineSerializerForViewing(data, many=True)
        return HttpResponse(json.dumps(serializer_data.data))
    
@csrf_exempt
def update_medicine_pharamacist_view(request):
    if request.method == "PUT":
        received_data = json.loads(request.body)
        get_medicine_id = received_data["medicineid"]
        get_status = received_data["status"]
        get_rate = received_data['total_rate']
        data = MedicinesModel.objects.filter(Q(medicineid__exact=get_medicine_id)).update(med_status=get_status, total_rate=get_rate)
        return HttpResponse(json.dumps({"status":"Updation successful"}))
    else:
        return HttpResponse(json.dumps({"status":"updation unsuccessful"}))

@csrf_exempt
def view_users_assistant_view(request):
    if request.method=="POST":
        users = list(UserRegistrationModel.objects.values_list('name', flat=True))
        doctors = list(DoctorRegistrationModel.objects.filter(Q(role="Doctor")).values_list('name', flat=True))
        return HttpResponse(json.dumps({"users":users, "doctors":doctors}))
    else:
        return HttpResponse(json.dumps({"status":"Retrieval unsuccessful"}))

@csrf_exempt
def save_results_view(request):
    if request.method=="POST":
        received_data = json.loads(request.body)
        serializer_data = DoctorAppoinmentSerilaizer(data=received_data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"Saving successful"}))
    else:
        return HttpResponse(json.dumps({"status":"Saving unsuccessful"}))