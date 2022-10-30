from django.shortcuts import render

# Create your views here.

def handler404(request, exception):
	return render(request, 'adminlte/page404.html')

def handler500(request):
	return render(request, 'adminlte/page500.html')