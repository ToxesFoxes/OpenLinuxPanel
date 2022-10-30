from django.shortcuts import render
from adminlte.config import config
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
	# navbar_skin = 'navbar-dark bg-dark'
	return render(request, 'dashboard/index.html', {
		'config': config(request),
		'user': request.user,
	})
	# return render(request, 'dashboard/index.html')
