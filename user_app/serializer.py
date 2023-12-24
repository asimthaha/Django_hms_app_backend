from rest_framework import serializers
from .models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrationModel
        fields=(
            'userid','name','email','password','phone'
        )
        
        
class DoctorAppoinmentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = BookDoctorModel
        fields = '__all__'