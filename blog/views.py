from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'

    def get(self, *args, **kwargs):
        response = super(HomePage, self).get(self, *args, **kwargs)
        return response


