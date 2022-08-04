from datetime import datetime, timedelta
import logging
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from user.models import User
from user.utils import JWTService
from django.conf import settings

logger = logging.getLogger('django')


class RegistrationAPIView(APIView):
    def post(self, request):
        """
        Register user using post api and serializer
        :param request:
        :return:
        """
        try:
            user_serializer = UserSerializer(data=request.data)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
            mail_subject = "Verification mail"
            token = JWTService.encode_token(payload={'id': user_serializer.data.get("id"),
                                                     'username': user_serializer.data.get('username')
                                                     # 'exp': datetime.now() + timedelta(minutes=60)
                                                     })
            mail_message = f"Click on this http://127.0.0.1:8000/user/verify/{token}"
            send_mail(mail_subject,
                      mail_message,
                      settings.EMAIL_HOST_USER,
                      [user_serializer.data.get("email")], fail_silently=False)
            return Response({"message": "Data save successfully ", "data": user_serializer.data}, status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": "Unexpected error"}, status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        """
        Login user using post api
        :param request:
        :return:
        """
        try:
            info = request.data
            login_user = authenticate(username=info.get("username"), password=info.get("password"))
            if login_user is not None:
                token = JWTService.encode_token(payload={'user_id': login_user.id, 'username': login_user.username})
                payload = {'token': token}
                return Response({'message': 'Login Successfully', 'data': payload}, status.HTTP_200_OK)
            else:
                return Response({'message': 'User not registered'}, status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'Unexpected error'}, status.HTTP_400_BAD_REQUEST)


class VarifyUser(APIView):
    """
    Validating the token if the user is valid or not
    """

    def get(self, request, token):
        try:
            decode_token = JWTService.decode_token(token=token)
            user = User.objects.get(username=decode_token.get('username'))
            user.is_verify = True
            user.save()
            return Response({"message": "Validation Successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            logging.error(e)
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
