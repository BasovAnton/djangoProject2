from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from blog.models import Note
from blog_api import serializers
from blog.models import Note
from rest_framework.generics import ListAPIView

class NoteListCreateAPIView(APIView):
    """ Представление, которое позволяет вывести весь список записей и добавить новую запись. """

    def get(self, request: Request):
        objects = Note.objects.all()
        note_serializer = serializers.NoteSerializer(instance=objects, many=True,)

        return Response(note_serializer.data)

    def post(self, request: Request):
        serializer = serializers.NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(author = request.user)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

class NotePublicListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

class NoteDetailAPIView(APIView):
    """ Представление, которое позволяет вывести отдельную запись. """
    def get(self, request, pk):  # todo path param
        # note = Note.objects.get(pk=pk)
        note = get_object_or_404(Note, pk=pk)

        return Response(serializers.note_created(note))
