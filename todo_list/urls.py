from django.urls import path
from rest_framework.generics import CreateAPIView
from .views import  api_over,TaskListView,TaskDetailView,CreateTaskView, DeleteTaskView,UpdateTaskView
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('',api_over,name='api_overview'),
    path('tasks/',TaskListView.as_view(),name='tasks-list'),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='detail_task'),
    path('create-task/',CreateTaskView.as_view(),name='create-task'),
    path('update-task/<int:pk>/',UpdateTaskView.as_view(),name='update-task'),
    path('delete-task/<int:pk>/',DeleteTaskView.as_view(),name='delete-task'),
]
urlpatterns = format_suffix_patterns(urlpatterns)