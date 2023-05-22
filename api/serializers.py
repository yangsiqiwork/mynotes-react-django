from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer): #serializer for specifi model
    class Meta:
        model = Note
        fields = '__all__' #specify ['body', 'up']