from django.shortcuts import render
from adminlte.config import config
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
	# navbar_skin = 'navbar-dark bg-dark'
	return render(request, 'dashboard/pages/index.html', {
		'config': config(request),
		'user': request.user,
		'overview': {
			'sites': {
				'value': 1,
				'style': {
					'color': 'bg-white',
					'icons': {
						'top': 'fa-globe',
						'footer':'fa-arrow-right',
					}
				},
				'text': {
					'main_title': 'Sites',
					'footer_title': 'View all',
				}
			},
			'databases': {
				'value': 2,
				'style': {
					'color': 'bg-white',
					'icons': {
						'top': 'fa-database',
						'footer':'fa-arrow-right',
					}
				},
				'text': {
					'main_title': 'Databases',
					'footer_title': 'View all',
				}
			},
			'ftp': {
				'value': 3,
				'style': {
					'color': 'bg-white',
					'icons': {
						'top': 'fa-arrow-down-up-across-line',
						'footer':'fa-arrow-right',
					}
				},
				'text': {
					'main_title': 'FTP',
					'footer_title': 'Manage access',
				}
			},
			'ssh': {
				'value': 4,
				'style': {
					'color': 'bg-white',
					'icons': {
						'top': 'fa-terminal',
						'footer':'fa-arrow-right',
					}
				},
				'text': {
					'main_title': 'SSH',
					'footer_title': 'Manage access',
				}
			},
			'email': {
				'value': 5,
				'style': {
					'color': 'bg-white',
					'icons': {
						'top': 'fa-envelope',
						'footer':'fa-arrow-right',
					}
				},
				'text': {
					'main_title': 'Email',
					'footer_title': 'View',
				}
			},
		}
	})
