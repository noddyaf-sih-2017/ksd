from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
is_a_disappointment = False

def render_page(request):
	return render(request, 'jhol.html')

def not_a_disappointment(request):
	is_a_disappointment = False
	print("hello")
	return render(request, "jhol.html")

def disappointment(request):
	is_a_disappointment = True
	print("goodbye")
	return render(request, "jhol.html")