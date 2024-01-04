from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from user_app.models import *
from user_app.serializer import *
from django.db.models import Q
import joblib
import os
import numpy as np
from rest_framework.views import APIView

# Create your views here.
@csrf_exempt
def registerView(request):
    if request.method=="POST":
        data = json.loads(request.body)
        serializer_data = UserRegistrationSerializer(data=data)
        print(serializer_data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"User data Added Successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"User data - Unsuccessful"}))

@csrf_exempt
def loginView(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        getEmail = data['email']
        getPassword = data['password']
        loginData = UserRegistrationModel.objects.filter(Q(email__exact=getEmail) & Q(password__exact = getPassword)).values()
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
def appointDoctorView(request):
    if request.method=="POST":
        data = json.loads(request.body)
        serializer_data = DoctorAppoinmentSerilaizer(data=data)
        print(serializer_data)
        if serializer_data.is_valid():
            serializer_data.save()
            return HttpResponse(json.dumps({"status":"Appoinment Successful"}))
        else:
            return HttpResponse(json.dumps({"status":"Appoinment Unsuccessful"}))
        
@csrf_exempt
def predictHeartView(request):
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
def displayDoctorBookingView(request):
    if request.method == "GET":
        data = BookDoctorModel.objects.all()
        data = DoctorAppoinmentSerilaizer(data, many=True)
        return HttpResponse(json.dumps(data.data))