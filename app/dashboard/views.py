from django.shortcuts import render
from adminlte.config import config


def index(request):
	# navbar_skin = 'navbar-dark bg-dark'
	return render(request, 'dashboard/index.html', {
		"config": config(request)
	})
	# return render(request, 'dashboard/index.html')
