from rest_framework import serializers
from user_app.models import *
from staff_app.models import *
from user_app.serializer import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegistrationModel
        # fields=(
        #     'satffid','photo','name','username','speciality','startYear','qualification','role','password'
        # )
        
        fields = '__all__'
        
        
class BookingSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer(source='userid', read_only=True)
    class Meta:
        model = BookDoctorModel
        fields='__all__'

class ViewBookingDataOfPatientsWhileSearch(serializers.ModelSerializer):
    doctor= DoctorSerializer(source='doctorid', read_only=True)
    class Meta:
        model=BookDoctorModel
        fields='__all__'

class searchPatientDataSerializer(serializers.ModelSerializer):
    bookings= ViewBookingDataOfPatientsWhileSearch(read_only=True, many=True)
    results = ResultSerializer(read_only=True, many=True)
    medicines= MedicineSerializer(read_only=True, many=True)
    class Meta:
        model = UserRegistrationModel
        fields='__all__'