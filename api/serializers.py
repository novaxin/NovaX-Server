# serializers.py
from rest_framework import serializers
from .models import Note, Command

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','note', 'likes', 'dislikes', 'commend_count','views', 'created']

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ['id','note', 'command', 'created']
