from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	data = "haha"
	return render(request, 'djaton/index.html', {'data': data})