from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse('Hello World, you are checking your app')

def myfirstshtml(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def mymaster(request):
    template=loader.get_template('master.html')
    return HttpResponse(template.render())