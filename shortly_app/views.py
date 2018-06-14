from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index, Hello World")

def detail(request, id):
    return HttpResponse("Detail, Hello World")

def new(request):
    return HttpResponse("New, Hello World")
