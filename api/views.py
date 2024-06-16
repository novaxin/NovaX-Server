from django.shortcuts import render
from django.http import HttpResponse
from .models import Note,Command
from .serializers import NoteSerializer,CommandSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User


from django.shortcuts import get_object_or_404

@api_view(['POST'])
def postnote(request):
    data = request.data
    username = data.get('user')
    user = get_object_or_404(User, username=username)
    note_data = {
        'user': user.id,
        'note': data.get('note'),
    }
    serializer = NoteSerializer(data=note_data)
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

@api_view(['GET'])
def display_user_note(request, username):
    user = get_object_or_404(User, username=username)
    notes = Note.objects.filter(user=user)
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
    command = request.data.get('command', '')
    username = request.data.get('user', '')
    user = get_object_or_404(User, username=username)

    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        return Response({"error": "Note does not exist"}, status=status.HTTP_404_NOT_FOUND)

    data = {
        'note': note_id,
        'command': command,
        'user': user.id  # Include 'user' field in data dictionary
    }

    serializer = CommandSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        update_command_count(note_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username and password:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return Response({'message': 'User authenticated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logout(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'User is not logged in'}, status=status.HTTP_400_BAD_REQUEST)
