from django.shortcuts import render
from shreya import views as vue

def render_main(request):
    return render(request, 'index.html')

