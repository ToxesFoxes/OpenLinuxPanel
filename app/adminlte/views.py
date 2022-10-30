from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from adminlte.forms import UserLoginForm
# Create your views here.

def handler404(request, exception):
	return render(request, 'adminlte/page404.html')

def handler500(request):
	return render(request, 'adminlte/page500.html')
	
class LoginUser(LoginView):
	form_class = UserLoginForm
	template_name = 'adminlte/login.html'
	def get_success_url(self):
		return reverse_lazy('index')