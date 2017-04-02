from django.shortcuts import render

def render_main(request):
    render(request, 'index.html')

