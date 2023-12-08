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

# Create your views here.
@csrf_exempt
def registerView(request):
    if request.method=="POST":
        data = json.loads(request.body)
        serializer_data = UserRegistrationSerializer(data=data)
        print(serializer_data)
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
        print(data)
        serializer_data = DoctorAppoinmentSerilaizer(data=data)
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
        recieved_data = json.loads(request.body)
        
        sex=recieved_data['sex']
        if sex== "Male":
            sex=1
        elif sex=="Female":
            sex=0
        
        cp=recieved_data['cp']
        if cp == "No Pain":
            cp=4
        elif cp == "Unusual Chest Pain":
            cp=3
        elif cp == "Non-Heart related Chest Pain":
            cp=2
        elif cp == "Typical Chest Pain":
            cp=1
            
        restECG=recieved_data['restecg']
        if restECG == "Left Chamber of the Heart has Thickened Walls":
            restECG = 1
        elif restECG == "Abnormality in Heart's Electrical Signals":
            restECG =2
        elif restECG == "No Significant Abnormalities Detected":
            restECG = 0
        
        slope=recieved_data['slope']
        if slope == "It Goes Down (Like a Hill)":
            slope=1
        elif slope == "It Stays Flat (Like Level Ground)":
            slope=2
        elif slope == "It Goes Up (Like an Incline)":
            slope =3
            
        thal = recieved_data['thal']
        if thal == "Normal Blood Flow" or "NULL":
            thal=3
        elif thal == "No Blood Flow in Some Part of the Heart (Fixed Defect)":
            thal=6
        elif thal == "Abnormal Blood Flow that Can Be Reversed (Reversible Defect)":
            thal=7
        
        exang =recieved_data['exang']
        if exang == "Yes":
            exang=1
        elif exang == "No":
            exang=0
            
        fbs = recieved_data['fbs']
        if fbs == "True":
            fbs=1
        elif fbs == "False":
            fbs = 0
        
        input_features = [
            float(recieved_data.get('age')),
            sex,
            cp,
            float(recieved_data.get('trestbps')),
            float(recieved_data.get('chol')),
            fbs,
            restECG,
            float(recieved_data.get('thalach')),
            exang,
            float(recieved_data.get('oldpeak')),
            slope,
            float(recieved_data.get('ca')),
            thal
        ]

        # Convert input_features to a NumPy array and reshape it
        input_data = np.array(input_features).reshape(1, -1)

        # Predict using the preloaded model
        prediction = model.predict(input_data)

        result = "The person has Heart Disease" if prediction[0] == 0 else "The person does not have a Heart Disease"

        # Tips and links
        tips_category = 'management_tips' if prediction[0] == 0 else 'prevention_tips'

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
            "heart_disease_management": "https://www.youtube.com/watch?v=IMBpwpf5crU",
            "heart_disease_prevention": "https://www.youtube.com/watch?v=B6UYNZLpAMs"
        }

        return HttpResponse(json.dumps({
            'result': result,
            'tips': tips[tips_category],
            'youtube_links': youtube_links
        }))
