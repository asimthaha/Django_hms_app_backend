from rest_framework import serializers
from user_app.models import *
from staff_app.models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegistrationModel
        # fields=(
        #     'satffid','photo','name','username','speciality','startYear','qualification','role','password'
        # )
        
        fields = '__all__'
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDoctorModel
        fields='__all__'