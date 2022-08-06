import jwt
import logging
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings


class JWTService:
    """
    Encoding and decoding using JWT
    """

    @staticmethod
    def encode_token(payload):
        """
        Encoding
        :return:
        """
        try:
            if payload.get('exp') is None:
                payload.update({"exp": settings.JWT_EXPIRING_TIME})

            token_encoded = jwt.encode(payload, settings.JWT_SECRET_KEY,
                                       algorithm="HS256")
            return token_encoded
        except Exception as e:
            logging.exception(e)
            return Response({'Message': 'Unexpected error'}, status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def decode_token(token):
        """
        Decoding
        :return:
        """
        try:
            token_decode = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            return token_decode
        except jwt.exceptions.ExpiredSignatureError as e:
            logging.exception(e)
            return Response({'Message': 'ExpiredSignatureError'})
        except jwt.exceptions.InvalidTokenError as e:
            logging.exception(e)
            return Response({'Message': 'InvalidTokenError'})
        except Exception as e:
            logging.exception(e)
            return Response({'Message': 'Unexpected error'})

