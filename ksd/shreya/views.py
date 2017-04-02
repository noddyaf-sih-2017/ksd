from django.shortcuts import render
from django.http import HttpResponse
from shreya import models
from shreya import canned as can

# Create your views here.
is_a_disappointment = 0

def get_disappointment():
	return is_a_disappointment

def render_page(request):
	return render(request, 'jhol.html')

def not_a_disappointment(request):
	can.set_ml_status(True)
	return render(request, "jhol.html")

def disappointment(request):
	can.set_ml_status(False)
	return render(request, "jhol.html")
