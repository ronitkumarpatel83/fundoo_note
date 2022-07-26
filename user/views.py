from .models import User
import logging
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

log = '%(lineno)d : %(asctime)s : %(message)s'
logging.basicConfig(filename='user_views.log', filemode='a', format=log, level=logging.DEBUG)


class RegistrationAPIView(APIView):
    def post(self, request):
        try:
            user_serializer = UserSerializer(data=request.data)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
            return Response({"message": "Data save successfully ",
                             "data": user_serializer.data}, status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": "Unexpected error"}, status.HTTP_401_UNAUTHORIZED)


class LoginAPIView(APIView):
    def post(self, request):
        try:
            info = request.data
            login_user = authenticate(username=info.get("username"), password=info.get("password"))
            if login_user is not None:
                return Response({'message': f'User {login_user.username} is successfully login'}, status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid username/password'}, status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'Unexpected error'}, status.HTTP_400_BAD_REQUEST)


# class ChangePasswordAPIView(APIView):
#     def post(self, request):
#         try:
#             info = request.data
#             user = User.objects.get(username=info.get('username'))
#             user.set_password(info.get('new_password'))
#             user.save()
#             return Response({'message': 'Successfully change new password'})
#         except Exception as e:
#             print(e)
#             return Response({'message': 'Something went wrong !!'})
