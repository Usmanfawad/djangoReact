from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Initializing this beautiful application Guys")

def detail(request, question_id):
    return HttpResponse("")