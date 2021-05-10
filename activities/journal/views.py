from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def index(req):
    return render(req, 'journal/index.html', context)

def show(req, id):
    return render(req, 'journal/show.html')

