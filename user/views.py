# from django.shortcuts import render
import json
import logging
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='user_views.log', filemode='a', format=log, level=logging.DEBUG)


class RegistrationAPIView(APIView):
    def post(self, request):
        try:
            info = request.data
            user_registration = User.objects.create_user(username=info.get("username"),
                                                         password=info.get("password"),
                                                         email=info.get("email"),
                                                         first_name=info.get("first_name"),
                                                         last_name=info.get("last_name"),
                                                         phone_number=info.get("phone_number"),
                                                         location=info.get("location"))
            user_registration.save()
            return JsonResponse({"message": f"Data save successfully {user_registration.username}",
                                 "data": {"id": user_registration.id}}, status=201)
        except Exception as e:
            logging.exception(e)
            return JsonResponse({"message": "Unexpected error"}, status=400)


class LoginAPIView(APIView):
    def post(self, request):
        try:
            info = request.data
            login_user = authenticate(username=info.get("username"), password=info.get("password"))
            # login_user = authenticate(**body)
            if login_user is not None:
                return JsonResponse({'message': f'User {login_user.username} is successfully login'}, status=200)
            else:
                return JsonResponse({'message': 'Invalid username/password'}, status=200)
        except Exception as e:
            logging.exception(e)
            return JsonResponse({'message': 'Unexpected error'}, status=400)


class ChangePasswordAPIView(APIView):
    def post(self, request):
        try:
            info = request.data
            print(info)
            user = User.objects.get(username=info.get('username'))
            user.set_password(info.get('new_password'))
            user.save()
            return JsonResponse({'message': 'Successfully change new password'})
        except Exception as e:
            print(e)
            return JsonResponse({})
