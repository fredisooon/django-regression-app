from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing(request):
    return render(request, "welcome/landing.html")

def workspace(request):
    return render(request, "welcome/workspace.html")