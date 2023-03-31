from rest_framework.response import Response

from blog.models import BlogPost
from .twilio_utils import send_otp_sms
from blog.serializers import BlogPostSerializer
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework.views import APIView
from .models import CustomUser
import random
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .serializers import VerifyOTPSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer
from rest_framework import status




class Registrationview(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        phone_number = request.data['phone_number']
        send_otp_sms(phone_number)
        
        serializer.save()
        
        
        return Response({'message':'Registration successfull'})


class VerifyView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = VerifyOTPSerializer

    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')

        try:
            user = CustomUser.objects.get(phone_number=phone_number, otp=otp)
            user.otp=''
            user.save()
            return Response({'message':'phone number verified successfully'})
        except CustomUser.DoesNotExist:
            raise ValidationError



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class BlogPostListView(APIView):
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request    ):
        stu = BlogPost.objects.all()
        serializer = BlogPostSerializer(stu, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Posted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors) #status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = True, format = None):
        id = pk
        stu = BlogPost.objects.get(id=id)
        serializer = BlogPostSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Posted'})
        return Response(serializer.error_messages)

    def patch(self, request, pk = True, format= None):
        id = pk
        stu = BlogPost.objects.get(pk=id)
        serializer = BlogPostSerializer(stu, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Posted'})
        return Response(serializer.errors)

    def delete(self, request, pk = True, format= None):
        id = pk
        stu = BlogPost.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

    


