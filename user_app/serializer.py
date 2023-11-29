from rest_framework import serializers
from .models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields=(
            'userid','name','email','password','phone','address',
        )
        
        
class DoctorAppoinmentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = BookDoctorModel
        fields = ('time','date')