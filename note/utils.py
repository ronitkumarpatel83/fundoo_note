import json
import logging
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from user.utils import JWTService
from note.redis_cache import RedisFunction


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


class RedisNoteAPI:

    def __init__(self):
        self.redis_obj = RedisFunction()

    def get_note(self, user):
        data = self.redis_obj.get_key(user)
        if data is None:
            return {}
        return json.loads(data)

    def create_note(self, user_id, note_id):
        data = self.get_note(user_id)
        data.update({note_id.get('id'): note_id})
        self.redis_obj.set_key(user_id, json.dumps(data))

    def update_note(self, notes):
        user_id = notes.get('user')
        id = str(notes.get('id'))
        note_dict = json.loads(self.redis_obj.get_key(user_id))
        if note_dict.get(id):
            note_dict.update({id: notes})
            self.redis_obj.set_key(user_id, json.dumps(note_dict))
        else:
            print("data not found")

    def delete_note(self, user_id, note_id):
        note_dict = json.loads(self.redis_obj.get_key(user_id))
        if note_dict.get(str(note_id)):
            note_dict.pop(str(note_id))
            self.redis_obj.set_key(user_id, json.dumps(note_dict))
