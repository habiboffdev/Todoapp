from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class OtherProjects(TemplateView):
    template_name = 'other.html'