import jwt
import logging
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from user.utils import JWTService


def verify_token(function):
    """
    Token verification and authorization
    :param function:
    :return:
    """
    def wrapper(self, request):
        if 'HTTP_TOKEN' not in request.META:
            resp = Response({'message': 'Token not provided in the header'})
            resp.status_code = 400
            logging.info('Token not provided in the header')
            return resp
        token = request.META.get("HTTP_TOKEN")
        payload = JWTService.decode_token(token=token)
        request.data.update({'user': payload.get('user_id')})

        return function(self, request)

    return wrapper
