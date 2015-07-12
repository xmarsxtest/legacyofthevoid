from django.shortcuts import render_to_response
from django.http import HttpResponse


def home(request):
	template = 'home.html'
	return render_to_response(template)