from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aweb(request):
    return HttpResponse("Hello, This is the aweb view!, FINISHED")