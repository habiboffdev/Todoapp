from django.urls import path
from .views import HomePageView,OtherProjects
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('other_projects',OtherProjects.as_view(),name='other_projects')
]