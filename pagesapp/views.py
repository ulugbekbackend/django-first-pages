from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexPageView(TemplateView):
    template_name='index.html'

class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'
    
class ServisesPageView(TemplateView):
    template_name='servises.html'