from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return HttpResponse("<h1>Hello! Ready to start with your activities?</h1>")

def show(req, id):
    return HttpResponse(f'<h3>Activity number {id}</h3>')

