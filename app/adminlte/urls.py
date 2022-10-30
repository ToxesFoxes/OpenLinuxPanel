from django.urls import path
from adminlte.views import LoginUser


urlpatterns = [
	path('login/', LoginUser.as_view(), name='login'),
	path('logout/', LoginUser.as_view(), name='logout'),
]