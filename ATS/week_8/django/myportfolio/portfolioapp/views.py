from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def index(request):
    return render(request, 'portfolioapp/home.html')

def components(request):
    return render(request, 'portfolioapp/components.html')