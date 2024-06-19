from rest_framework import serializers
from .models import Note, Command, LikeOrDislike

class NoteSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Note
        fields = ['id', 'user','username', 'note', 'likes', 'dislikes', 'commend_count', 'views', 'created']

class CommandSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Command
        fields = ['id', 'user','username', 'note', 'command', 'created']  

class LikeOrDislikeSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    note_id = serializers.ReadOnlyField(source='note.id')

    class Meta:
        model = LikeOrDislike
        fields = ['id', 'user', 'username', 'note', 'note_id', 'type']