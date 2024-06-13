from django.shortcuts import render
from django.http import HttpResponse
from .models import Note,Command
from .serializers import NoteSerializer,CommandSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random
from django.shortcuts import get_object_or_404




@api_view(['POST'])
def postnote(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def display(request):
    notes = Note.objects.order_by('-created')
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def random(request):
    notes = Note.objects.order_by('?')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)



# comment views 



def update_command_count(note_id):
    note = get_object_or_404(Note, id=note_id)
    count_commands = Command.objects.filter(note_id=note_id).count()
    note.commend_count = count_commands
    note.save()
    print("saved")



@api_view(['GET'])
def display_command(request, note_id):
    filter_option = request.GET.get('filter', 'recent')
    if filter_option == 'recent':
        commands = Command.objects.filter(note_id=note_id).order_by('-created')
    elif filter_option == 'oldest':
        commands = Command.objects.filter(note_id=note_id).order_by('created')
    elif filter_option == 'random':
        commands = Command.objects.filter(note_id=note_id).order_by('?')
    else:
        commands = Command.objects.filter(note_id=note_id)

    serializer = CommandSerializer(commands, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_command(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        return Response({"error": "Note does not exist"}, status=status.HTTP_404_NOT_FOUND)

    data = {
        'note': note_id,
        'command': request.data.get('command', ''),
    }
    
    serializer = CommandSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        update_command_count(note_id)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










