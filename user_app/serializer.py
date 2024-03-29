from rest_framework import serializers
from user_app.models import *
from staff_app.models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrationModel
        fields=(
            'userid','name','email','password','phone'
        )

class StaffRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegistrationModel
        fields=(
            'staffid','name'
        )

class UserRegistrationSerializerForAppointment(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrationModel
        fields=(
            'userid','name'
        )

class DoctorAppoinmentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model= BookDoctorModel
        fields= '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsModel
        fields = '__all__'

class ResultSerializerV2(serializers.ModelSerializer):
    doctors= StaffRegistrationSerializer(source='doctorid', read_only=True)
    class Meta:
        model = ResultsModel
        fields=(
            '__all__'
        )

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinesModel
        fields = '__all__'

class DisableBookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDoctorModel
        fields = '__all__'

class MedicineSerializerForViewing(serializers.ModelSerializer):
    user = UserRegistrationSerializer(source='userid', read_only=True)
    class Meta:
        model = MedicinesModel
        fields = '__all__'

class RazorpayOrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()


class TranscationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionModel
        fields = ["transaction_id", "user_id", "payment_id", "order_id", "signature", "amount"]
