from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request1):
	var='<h1>Radhe Radhe Maharaj ji   Radhe Radhe</h1>'
	return HttpResponse(var)
