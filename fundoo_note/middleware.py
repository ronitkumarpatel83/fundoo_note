import logging
from user.utils import JWTService
from rest_framework import status
from rest_framework.response import Response
from user.models import Log


class NoteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def process_exception(self, request, exception):
        logging.exception(exception)

    def __call__(self, request):
        token = request.META.get("HTTP_TOKEN")
        user_id = JWTService.decode_token(token).get('user_id')
        if user_id:
            Log.objects.create(token=token, user_id_id=user_id)

        response = self.get_response(request)
        return response
