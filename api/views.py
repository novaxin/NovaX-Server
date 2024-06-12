from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random




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



