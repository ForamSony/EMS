from rest_framework.serializers import ModelSerializer
from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeRegistrationSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return Employee.objects.create_user(**validated_data)


class EmployeeLoginSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = Employee
        fields = ["email", "password"]
