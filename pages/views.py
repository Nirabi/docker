from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def Home_Page_View(request):
    return HttpResponse("Hello, world")
