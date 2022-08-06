import logging
from note.models import Note
from rest_framework.views import APIView
from note.serializers import NotesSerializers
from rest_framework.response import Response
from rest_framework import status
from user.utils import JWTService
from note.utils import verify_token

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
            notes = Note.objects.filter(user=user_id)
            serializer = NotesSerializers(instance=notes, many=True)
            return Response({'data': serializer.data}, status.HTTP_200_OK)
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
            # print(request.data)
            serializer = NotesSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
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
            print(notes)
            serializer = NotesSerializers(notes, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data}, status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self, request):
        """
        Deletong data from table
        :param request:
        :return:
        """
        try:
            notes = Note.objects.get(id=request.data.get('id'))
            notes.delete()
            return Response({'data': 'deleted'}, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status.HTTP_400_BAD_REQUEST)
