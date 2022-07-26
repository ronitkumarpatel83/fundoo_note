import logging
from note.models import Note
from rest_framework.views import APIView
from note.serializers import NotesSerializers
from rest_framework.response import Response
from rest_framework import status

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='note.log', filemode='a', format=log, level=logging.DEBUG)


class NoteDetails(APIView):

    def get(self, request):
        try:
            # notes = Note.objects.get(id=1)
            notes = Note.objects.all()
            serializer = NotesSerializers(instance=notes, many=True)
            return Response({'data': serializer.data}, status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status=400)

    def post(self, request):
        try:
            # user = User.objects.get(pk=request.data.get('user'))
            # note = Note.objects.create(user=user, title=request.data.get('title'),
            #                             description=request.data.get('description'))
            # note = Note.objects.create(user_id=request.data.get('user'), title=request.data.get('title'),
            #                             description=request.data.get('description'))
            serializer = NotesSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": f"Data save successfully",
                             "data": serializer.data}, status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response({"message": "Unexpected error"}, status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            notes = Note.objects.get(id=request.data.get('id'))
            print(notes)
            serializer = NotesSerializers(notes, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data}, status.HTTP_202_ACCEPTED)
        except Note.DoesNotExist as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            notes = Note.objects.get(id=request.data.get('id'))
            notes.delete()
            return Response({'data': 'deleted'}, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.exception(e)
            return Response({'message': 'unexpected error'}, status.HTTP_400_BAD_REQUEST)
