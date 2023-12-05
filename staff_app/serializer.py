from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegistrationModel
        fields=(
            'doctorid','name','username','speciality','startYear','qualification','role','password'
        )