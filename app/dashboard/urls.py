from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('websites/', views.websites, name='websites'),
    path('databases/', views.default, name='databases'),
    path('files/', views.default, name='files'),
    path('ftp/', views.default, name='ftp'),
    path('ssh/', views.default, name='ssh'),
    path('mail/', views.default, name='mail'),
	path('login/', views.LoginUser.as_view(), name='login'),
]
