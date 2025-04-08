# todo/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializers import ToDoSerializer

# List all To-Do items
class TodoListView(APIView):
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

# Retrieve, update, or delete a To-Do item
class TodoDetailView(APIView):
    def get(self, request, id):
        try:
            todo = ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            todo = ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            todo = ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)