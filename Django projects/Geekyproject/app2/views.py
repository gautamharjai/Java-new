from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def learn_django(request):
    return HttpResponse("Hello Django")

def learn_html(request):
    return HttpResponse("<h1> Hello</h1>")

def learn_djhtml(request):
    a='<h1> Hello</h1>'
    return HttpResponse(a)

def learn_variable(request):
    b=10+10
    return HttpResponse(b)