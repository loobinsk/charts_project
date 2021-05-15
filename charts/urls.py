
from django.urls import path
from .views import dashboard, worker_statistics, teamleaders_list, teamleader_statistics, new_teamleader, new_worker, change_teamleader

urlpatterns = [
	path('', dashboard, name='dashboard'),
	path('new-teamleader/', new_teamleader, name='new_teamleader'),
	path('new-worker/', new_worker, name='new_worker'),
	path('my-teamleaders/', teamleaders_list, name='teamleaders-list'),
	path('worker-statistics/<slug>/', worker_statistics, name='worker-statistics'),
	path('change_teamleader/<worker>', change_teamleader, name='change_teamleader'),
	path('teamleader_statistics/<slug>/', teamleader_statistics, name='teamleader-statistics'),
]