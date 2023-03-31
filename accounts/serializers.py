from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','phone_number','location']

    


class VerifyOTPSerializer(serializers.Serializer):
    phone_number =  serializers.CharField()
    otp = serializers.CharField()

    def validate(self, data):
        phone_number = data.get('phone_number')
        otp = data.get('otp')

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError('user does not exist with the given phone number')
        if not user.check_otp(otp):
            raise serializers.ValidationError('invalid otp')
        
        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
