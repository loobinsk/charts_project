from django.contrib import admin
from .models import TestData, Worker, TeamLeader, HeadOfDeportment, Profile


class TestDataAdmin(admin.ModelAdmin):
	list_display = ['date', 'data1', 'data2', 'data3', 'data4', 'data5', 'worker']
	list_filter = ['worker', 'date', 'data1', 'data2', 'data3', 'data4', 'data5',]
	list_editable = ['data1', 'data2', 'data3', 'data4', 'data5', 'worker']
	search_fields = ['date', 'data1', 'data2', 'data3', 'data4', 'data5', 'worker']

admin.site.register(TestData, TestDataAdmin)


class WorkerAdmin(admin.ModelAdmin):
	list_display = ['user', 'teamleader',]
	list_filter = ['teamleader',]

admin.site.register(Worker, WorkerAdmin)

class TeamLeaderAdmin(admin.ModelAdmin):
	list_display = ['user', 'HeadOfDeportment',]
	list_filter = ['HeadOfDeportment',]

admin.site.register(TeamLeader, TeamLeaderAdmin)

admin.site.register(HeadOfDeportment)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'group',]
	list_filter = ['group',]

admin.site.register(Profile, ProfileAdmin)
