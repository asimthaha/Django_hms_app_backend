from rest_framework import serializers
from user_app.models import *
from staff_app.models import *
from user_app.serializer import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegistrationModel
        # fields=(
        #     'staffid','photo','name','username','speciality','startYear','qualification','role','password'
        # )
        
        fields = '__all__'

class DoctorSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegistrationModel
        fields=(
            'staffid','name'
        )
        
        
class BookingSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer(source='userid', read_only=True)
    class Meta:
        model = BookDoctorModel
        fields='__all__'

class BookingViewSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializerForAppointment(source='userid', read_only=True)
    class Meta:
        model = BookDoctorModel
        fields='__all__'

class ViewBookingDataOfPatientsWhileSearch(serializers.ModelSerializer):
    doctor= DoctorSerializerV2(source='doctorid', read_only=True)
    class Meta:
        model=BookDoctorModel
        fields='__all__'

class searchPatientDataSerializer(serializers.ModelSerializer):
    bookings= ViewBookingDataOfPatientsWhileSearch(read_only=True, many=True)
    results = ResultSerializer(read_only=True, many=True)
    medicines= MedicineSerializer(read_only=True, many=True)
    class Meta:
        model = UserRegistrationModel
        fields=(
            'userid','name', 'medicines', 'results', 'bookings'
        )

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsModel
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model= NotificationsModel
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model= PredictionModel
        fields = '__all__'

class BmiSerializer(serializers.ModelSerializer):
    class Meta:
        model= BmiModel
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer(source='user_id', read_only=True)
    class Meta:
        model= TransactionModel
        fields = '__all__'