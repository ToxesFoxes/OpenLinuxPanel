from django.shortcuts import render
from adminlte.config import config
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from adminlte.forms import UserLoginForm

overview = {
	'home': {
		'ignore': ['index'],
		'url': 'index',
		'style': {
			'icons': {
				'top': 'fa-house',
			}
		},
		'text': {
			'main_title': 'Home',
		}
	},
	'sites': {
		'value': 1,
		'url': 'websites',
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
		'url': 'databases',
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
	'files': {
		'ignore': ['index', 'all'],
		'value': 3,
		'url': 'files',
		'style': {
			'color': 'bg-white',
			'icons': {
				'top': 'fa-folder',
				'footer':'fa-arrow-right',
			}
		},
		'text': {
			'main_title': 'File Manager',
			'footer_title': 'Manage access',
		}
	},
	'ftp': {
		'value': 3,
		'url': 'ftp',
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
		'url': 'ssh',
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
		'url': 'mail',
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
@csrf_protect
def default(request):
	return render(request, 'dashboard/pages/default.html', {
		'config': config(request),
		'user': request.user,
		'page': {
			'name': 'Default Page',
			'url_name': request.resolver_match.url_name,
		},
		'hide_preloader': True,
		'overview': overview,
	})

@csrf_protect
def index(request):
	return render(request, 'dashboard/pages/index.html', {
		'config': config(request),
		'user': request.user,
		'page': {
			'name': 'Home',
			'url_name': request.resolver_match.url_name,
		},
		'hide_preloader': False,
		'overview': overview,
	})

@csrf_protect
def websites(request):
	return render(request, 'dashboard/pages/websites.html', {
		'config': config(request),
		'user': request.user,
		'page': {
			'name': 'Websites',
			'url_name': request.resolver_match.url_name,
		},
		'hide_preloader': True,
		'overview': overview,
	})

class LoginUser(LoginView):
	form_class = UserLoginForm
	template_name = 'dashboard/pages/login.html'
	def get_success_url(self):
		return reverse_lazy('index')