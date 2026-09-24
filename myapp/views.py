from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bweb(request):
    return HttpResponse("Hello, This is the bweb view, 完˙成")