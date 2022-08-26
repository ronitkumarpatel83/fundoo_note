from note.models import Note
from rest_framework import serializers


class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'user', 'title', 'description']


class ShareNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['user', 'id', 'collaborator']
