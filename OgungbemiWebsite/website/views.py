from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def page1(request):
    return render(request, "tsietsi.html")

def page2(request):
    return render(request, "impossible.html")

def page3(request):
    return render(request, "ghost.html")

def page4(request):
    return render(request, "sovenga.html")

def page5(request):
    return render(request, "contact.html")