from rest_framework import serializers
from user_app.models import *
from staff_app.models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrationModel
        fields=(
            'userid','name','email','password','phone'
        )
 
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsModel
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinesModel
        fields = '__all__'
