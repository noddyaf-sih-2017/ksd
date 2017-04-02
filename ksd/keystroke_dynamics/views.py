from django.shortcuts import render
from shreya import views as vue
from shreya import canned as can

def render_main(request):
	str = ""
	if can.query_ml_status():
		str = True
	else:
		str = False
	return render(request, 'index.html', {'status':str})

