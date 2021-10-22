from rest_framework import mixins
from django.http import request
from rest_framework.generics import ListAPIView,RetrieveAPIView, DestroyAPIView,RetrieveUpdateAPIView,CreateAPIView,UpdateAPIView
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
@api_view(["GET",])
def api_over(request):
    api_urls={
        'List_tasks':'/tasks/',
        'Detail_task':'/detail-task/<int:pk>',
        'Create':'/create-task/',
        'Delete':'/delete-task/<int:pk>',
        'Update': '/update-task/<int:pk>/'
    }
    return Response(api_urls)

class TaskListView(ListAPIView):
    queryset =Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer

class TaskDetailView(RetrieveAPIView):
     queryset =Todo.objects.all()
     serializer_class = TodoSerializer

class CreateTaskView(CreateAPIView):
    queryset =Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTaskView(RetrieveUpdateAPIView):
    
    queryset =Todo.objects.all()
    serializer_class = TodoSerializer
class DeleteTaskView(DestroyAPIView):
    
    queryset =Todo.objects.all()
    serializer_class = TodoSerializer