from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	return HttpResponse('hello')

def home(request):
	return render(request,'home.html')

def count(request):
	total_count = len(request.GET['text'])
	return render(request,'count.html',{'count':total_count})