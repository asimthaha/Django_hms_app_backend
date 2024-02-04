from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from user_app.models import *
from user_app.serializer import *
from django.db.models import Q
import joblib
import numpy as np
from .main import RazorpayClient
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@csrf_exempt
def register_view(request):
    if request.method=="POST":
        data = json.loads(request.body)
        serializer_data = UserRegistrationSerializer(data=data)
        print(serializer_data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"User data - unsuccessful"}))

@csrf_exempt
def login_view(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        getEmail = data['email']
        getPassword = data['password']
        loginData = UserRegistrationModel.objects.filter(Q(email__exact=getEmail) & Q(password__exact = getPassword)).values()
        loginData = list(loginData)
        return HttpResponse(json.dumps(loginData))
    
@csrf_exempt
def display_userdata_view(request):
    if request.method =="POST":
        received_data = json.loads(request.body)
        getUserid = received_data["userid"]
        data = UserRegistrationModel.objects.filter(Q(userid__exact=getUserid)).values()
        data = list(data)
        return HttpResponse(json.dumps(data))
    
@csrf_exempt
def update_userdata_view(request):
    if request.method == "PUT":      
        received_data = json.loads(request.body)
        getUserid = received_data["userid"]
        getName = received_data["name"]
        getEmail = received_data["email"]
        getPhone = received_data["phone"]
        getPassword = received_data["password"]
        getAddress = received_data["address"]
        data = UserRegistrationModel.objects.filter(Q(userid__exact=getUserid))
        data.update(name=getName,email= getEmail,phone=getPhone,password= getPassword, address=getAddress)
        return HttpResponse(json.dumps({"status":"Data updated successfully"}))

@csrf_exempt        
def bmi_calculator_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        getWeight = int(data["weight"])
        getHeight = int(data["height"])
        bmi = round(getWeight/((getHeight/100)**2))
        if bmi< 18.5:
            status = 'Underweight'
        elif (bmi>=18.5 and bmi<=24.9):
            status = 'Healthy'
        elif (bmi>=25.0 and bmi<=29.9):
            status = 'Overweight'
        else:
            status = 'Obese'
            
        return HttpResponse(json.dumps({"result":bmi, "status":status}))
    
@csrf_exempt
def appoint_doctor_view(request):
    if request.method=="POST":
        data = json.loads(request.body)
        serializer_data = DoctorAppoinmentSerilaizer(data=data)
        print(serializer_data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"Appoinment successful"}))
        else:
            return HttpResponse(json.dumps({"status":"Appoinment unsuccessful"}))
        
@csrf_exempt
def predict_heart_view(request):
    model = joblib.load("E:\\STUDY\\hms_backend\\user_app\\model.joblib")  # Load your saved model
    prediction = None

    if request.method == 'POST':
        data = json.loads(request.body)
        
        
        input_features = [
            float(data.get('age')),
            float(data.get('sex')),
            float(data.get('cp')),
            float(data.get('trestbps')),
            float(data.get('chol')),
            float(data.get('fbs')),
            float(data.get('restecg')),
            float(data.get('thalach')),
            float(data.get('exang')),
            float(data.get('oldpeak')),
            float(data.get('slope')),
            float(data.get('ca')),
            float(data.get('thal'))
        ]

        # Convert input_features to a NumPy array and reshape it
        input_data = np.array(input_features).reshape(1, -1)

        # Predict using the preloaded model
        prediction = model.predict(input_data)

        result = "The person has Heart Disease" if prediction[0] == 0 else "The person does not have a Heart Disease"

        # Tips and links
        tips_category = 'management_tips' if prediction[0] == 0 else 'prevention_tips'
        links_category = 'heart_disease_management' if prediction[0]==0 else 'heart_disease_prevention'

        tips = {
            "management_tips": [
                "Follow a heart-healthy diet rich in fruits, vegetables, and whole grains.",
                "Engage in regular exercise as recommended by your healthcare provider.",
                "Take prescribed medications as directed by your doctor.",
                "Practice stress-reduction techniques to manage stress levels.",
                "Schedule regular visits with your healthcare provider for monitoring."
            ],
            "prevention_tips": [
                "Maintain a balanced diet with fruits, vegetables, lean proteins, and healthy fats.",
                "Stay physically active to maintain a healthy weight and cardiovascular fitness.",
                "Avoid smoking and seek help to quit if needed.",
                "Limit alcohol consumption to moderate levels.",
                "Practice stress-relief techniques to reduce the impact of stress.",
                "Schedule regular health check-ups for early detection and prevention."
            ]
        }

        youtube_links = {
            "heart_disease_management": "https://www.youtube.com/watch?v=E0Am_KGBdUg",
            "heart_disease_prevention": "https://www.youtube.com/watch?v=_ePLBIDlChA"
        }

        return HttpResponse(json.dumps({
            'result': result,
            'tips': tips[tips_category],
            'youtube_links': youtube_links[links_category]
        }))
    
@csrf_exempt
def disable_appoinments_View(request):
    if request.method == "POST":
        received_data = json.loads(request.body)
        get_date = received_data['date']
        data = BookDoctorModel.objects.filter(Q(date__exact=get_date)).all()
        serialized_data = DisableBookingsSerializer(data, many=True)
        return HttpResponse(json.dumps(serialized_data.data))
    

@csrf_exempt
def view_results_user_view(request):
    if request.method=="POST":
        received_data = json.loads(request.body)
        get_userid = received_data["userid"]
        data = ResultsModel.objects.filter(Q(userid__exact=get_userid)).all()
        serializer_data = ResultSerializerV2(data, many=True)
        return HttpResponse(json.dumps(serializer_data.data))
    
@csrf_exempt
def view_medicine_user_view(request):
    if request.method=="POST":
        received_data = json.loads(request.body)
        get_userid = received_data["userid"]
        data = MedicinesModel.objects.filter(Q(userid__exact=get_userid)).all()
        serializer_data = MedicineSerializer(data, many=True)
        return HttpResponse(json.dumps(serializer_data.data))


rz_client = RazorpayClient()

@csrf_exempt
def create_order_view(request):
    if request.method == "POST":
        received_data = json.loads(request.body)
        razorpay_order_serializer = RazorpayOrderSerializer(
            data=received_data
        )
        if razorpay_order_serializer.is_valid():
            order_response = rz_client.create_order(
                amount=razorpay_order_serializer.validated_data.get("amount"),
                currency=razorpay_order_serializer.validated_data.get("currency")
            )
            response = {
                "status_code": status.HTTP_201_CREATED,
                "message": "order created",
                "data": order_response
            }
            return HttpResponse(json.dumps(response))
        else:
            response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": "bad request",
                "error": razorpay_order_serializer.errors
            }
            return HttpResponse(json.dumps(response))

@csrf_exempt
def verify_payment_view(request):
    if request.method == "POST":
        received_data = json.loads(request.body)
        transaction_serializer = TranscationModelSerializer(data=received_data)
        if transaction_serializer.is_valid():
            rz_client.verify_payment_signature(
                razorpay_payment_id = transaction_serializer.validated_data.get("payment_id"),
                razorpay_order_id = transaction_serializer.validated_data.get("order_id"),
                razorpay_signature = transaction_serializer.validated_data.get("signature")
            )
            transaction_serializer.save()
            response = {
                "status_code": status.HTTP_201_CREATED,
                "message": "transaction created"
            }
            return HttpResponse(json.dumps(response))
        else:
            response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": "bad request",
                "error": transaction_serializer.errors
            }
            return HttpResponse(json.dumps(response))
