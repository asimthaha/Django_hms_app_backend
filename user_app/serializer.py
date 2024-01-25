from rest_framework import serializers
from user_app.models import *
from staff_app.models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrationModel
        fields=(
            'userid','name','email','password','phone'
        )

class DoctorAppoinmentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model= BookDoctorModel
        fields= '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsModel
        fields = '__all__'

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
        fields = ["payment_id", "order_id", "signature", "amount"]