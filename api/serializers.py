from rest_framework import serializers
from .models import Note, Command

class NoteSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Note
        fields = ['id', 'user','username', 'note', 'likes', 'dislikes', 'commend_count', 'views', 'created']

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ['id', 'user', 'note', 'command', 'created']  
