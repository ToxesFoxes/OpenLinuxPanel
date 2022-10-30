from django.urls import path
from .views import SystemStatsView

urlpatterns = [
	path('system-stats/order/', SystemStatsView.as_view(), name='system-stats'),
]
