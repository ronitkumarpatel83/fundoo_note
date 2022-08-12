import logging
from note.models import Note
from rest_framework.views import APIView
from note.serializers import NotesSerializers
from rest_framework.response import Response
from rest_framework import status
from note.utils import verify_token, RedisNoteAPI

log = '%(lineno)d : %(asctime)s : %(message)s'
logging.basicConfig(filename='logfile.log', filemode='a', format=log, level=logging.DEBUG)


class NoteDetails(APIView):

    @verify_token
    def get(self, request):
        """
        Using GET method here for getting data from table
        :param request:
        :return:
        """
        try:
            user_id = request.data.get('user')
            # notes = Note.objects.filter(user=user_id)
            # serializer = NotesSerializers(instance=notes, many=True)
            # for key in serializer.data:
            #     RedisNoteAPI().create_note(user_id, note_id=dict(key))
            # data = [value for key, value in RedisNoteAPI().get_note(user_id).items()]
            data = RedisNoteAPI().get_note(user_id).values()
            return Response({"data": data}, status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status=400)

    @verify_token
    def post(self, request):
        """
        Storing data in table
        :param request:
        :return:
        """
        try:
            user_id = request.data.get('user')
            serializer = NotesSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            RedisNoteAPI().create_note(user_id, note_id=dict(serializer.data))
            return Response({"message": f"Data save successfully",
                             "data": serializer.data}, status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response({"message": "Unexpected error"}, status.HTTP_400_BAD_REQUEST)

    @verify_token
    def put(self, request):
        """
        Updating data in table
        :param request:
        :return:
        """
        try:
            notes = Note.objects.get(id=request.data.get('id'))
            serializer = NotesSerializers(notes, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            RedisNoteAPI().update_note(serializer.data)
            return Response({'data': serializer.data}, status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self, request):
        """
        Deleting data from table
        :param request:
        :return:
        """
        try:
            note = Note.objects.get(id=request.data.get('id'))
            RedisNoteAPI().delete_note(request.data.get('user'), note.id)
            note.delete()
            return Response({'data': 'deleted'}, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status.HTTP_400_BAD_REQUEST)
