from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_catches(request):
    return HttpResponse("Hello, Catches!")