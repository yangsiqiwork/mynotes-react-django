from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
# from rest_fr  amework.serializers import Serializer
from .serializers import NoteSerializer
# from api import serializers
# from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote
# # Create your views here.


# Create your views here.
# def getRoutes(request):

#     return JsonResponse('Our API', safe=False)

 
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


# # /notes GET
# # /notes POST
# # /notes/<id> GET
# # /notes/<id> PUT
# # /notes/<id> DELETE

@api_view(['GET'])
def getNotes(request):

    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True) #return back query set
    return Response(serializer.data)

    # if request.method == 'GET':
    #     return getNotesList(request)

    # if request.method == 'POST':
    #     return createNote(request)


@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

#     if request.method == 'GET':
#         return getNoteDetail(request, pk)

#     if request.method == 'PUT':
#         return updateNote(request, pk)

#     if request.method == 'DELETE':
#         return deleteNote(request, pk)


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid(): #model forms
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')

