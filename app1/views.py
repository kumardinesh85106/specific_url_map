from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>my first project</h1>')
def second(request):
    return HttpResponse('<h1>my second project</h1>')
