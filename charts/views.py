
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import TestData, Profile, TeamLeader, HeadOfDeportment, Worker
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def dashboard(request):
	'''information output to the main page'''

	#if the user is an employee, do the following:
	if request.user.profile.group == 0: 
		#script to create test data
		#for i in range(1, 30):
			#i = str(i)
			#if len(i) == 1:
				#i = f'0{str(i)}'
			#date = f'2021-05-{i}'
			#i = int(i)
			#new_data = TestData(
				#worker=request.user, 
				#data1=i+2, data2=i+1,
				 #data3=i+5, data4=i+7, 
				 #data5=i+12, date=date)
			#new_data.save()
			#end script

		data = TestData.objects.filter(worker__user=request.user).order_by('date')[:10]
		
		if request.method == 'POST':
			post_date1 = request.POST['date1']
			post_date2 = request.POST['date2']
			data = TestData.objects.filter(
				worker__user=request.user, 
				date__range=[post_date1, post_date2]
				).order_by('date').all()

		template = 'homepage/dashboard_for_workers.html' #html document for output
		context = {
			'data': data,
			} #transmitted variables for displaying information
		return render(request, template, context)


	#if the user is a team leader, do the following:
	elif request.user.profile.group == 1:
		data = TestData.objects.filter(
			worker__teamleader__user=request.user
			).order_by('date')[:10]

		workers = Worker.objects.filter(teamleader__user=request.user).all()

		if request.method == 'POST':
			post_date1 = request.POST['date1']
			post_date2 = request.POST['date2']
			data = TestData.objects.filter(
				worker__teamleader__user=request.user, 
				date__range=[post_date1, post_date2]
				).order_by('date').all()

		template = 'homepage/dashboard_for_team_leader.html'
		context = {
			'data': data,
			'workers': workers,
		}
		return render(request, template, context)


	#if the user is a head of deportment, do the following:
	elif request.user.profile.group == 2:
		return HttpResponseRedirect('my-teamleaders/')

@login_required
def worker_statistics(request, slug):
	'''function that displays statistics of a specific worker'''
	get_user = User.objects.get(username=slug)
	get_worker = Worker.objects.get(user=get_user)
	get_worker_data = TestData.objects.filter(
		worker=get_worker).order_by('date').all()
	teamleaders_list = TeamLeader.objects.filter(HeadOfDeportment__user=request.user).all()
	username = get_user.username

	if request.user.profile.group == 2:
		workers = Worker.objects.filter(teamleader__HeadOfDeportment__user=request.user).all()
	elif request.user.profile.group == 1:
		workers = Worker.objects.filter(teamleader__user=request.user).all()


	if request.method == 'POST':
		post_date1 = request.POST['date1']
		post_date2 = request.POST['date2']
		get_worker_data = TestData.objects.filter(
			worker=get_worker, 
			date__range=[post_date1, post_date2]
			).order_by('date').all()

	template = 'workers/worker_statistics.html'
	context={
		'worker': get_worker,
		'data': get_worker_data,
		'teamleaders': teamleaders_list,
		'username': username,
		'workers': workers,
		#'username': username,		
	}
	return render(request, template, context)

@login_required
def teamleaders_list(request):
	teamleaders_list = TeamLeader.objects.filter(HeadOfDeportment__user=request.user).all()
	template = 'account/teamleaders-list.html'
	get_data = TestData.objects.filter(worker__teamleader__HeadOfDeportment__user=request.user).order_by('date')[:10]
	workers = Worker.objects.filter(teamleader__HeadOfDeportment__user=request.user).all()

	if request.method == 'POST':
		post_date1 = request.POST['date1']
		post_date2 = request.POST['date2']
		get_data = TestData.objects.filter(
			worker__teamleader__HeadOfDeportment__user=request.user,
			date__range=[post_date1, post_date2]
			).order_by('date').all()

	context = {
		'teamleaders': teamleaders_list,
		'data': get_data,
		'workers': workers,
	}

	return render(request, template, context)

@login_required
def teamleader_statistics(request, slug):
	'''statistics of workers of a certain team leader'''
	teamleaders_list = TeamLeader.objects.filter(HeadOfDeportment__user=request.user).all()
	get_teamleader_user = User.objects.get(username=slug)
	get_teamleader = TeamLeader.objects.get(user=get_teamleader_user)
	get_teamleader_data = TestData.objects.filter(
		worker__teamleader=get_teamleader,
		).order_by('date')[:10]
	workers = Worker.objects.filter(teamleader=get_teamleader).all()

	if request.method == 'POST':
		post_date1 = request.POST['date1']
		post_date2 = request.POST['date2']
		get_data = TestData.objects.filter(
			worker__teamleader__HeadOfDeportment__user=request.user,
			date__range=[post_date1, post_date2]
			).order_by('date').all()


	template = 'account/teamleader-statistics.html'
	context = {
		'teamleaders': teamleaders_list,
		'temaleader': get_teamleader,
		'data': get_teamleader_data,
		'workers': workers,
	}

	return render(request, template, context)

@login_required
def new_teamleader(request):
	'''create new tl'''
	teamleaders_list = TeamLeader.objects.filter(HeadOfDeportment__user=request.user).all()
	get_data = TestData.objects.filter(
		worker__teamleader__HeadOfDeportment__user=request.user,
		).order_by('date').all()
	workers = Worker.objects.filter(teamleader__HeadOfDeportment__user=request.user).all()

	head_of_deportment = HeadOfDeportment.objects.get(user=request.user)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = User.objects.create_user(
			username=username, 
			password=password)
		user.save()

		user_profile = Profile(
			user=user, 
			group=1,
			)
		user_profile.save()

		teamleader = TeamLeader(user=user, HeadOfDeportment=head_of_deportment)
		teamleader.save()
		return HttpResponseRedirect('/')

	template = 'create/create-teamleader.html'
	context = {
		'teamleaders': teamleaders_list,
		'data': get_data,
		'workers': workers,
	}
	return render(request, template, context)

@login_required
def new_worker(request):
	'''create new worker'''
	teamleaders_list = TeamLeader.objects.filter(HeadOfDeportment__user=request.user).all()
	get_data = TestData.objects.filter(
		worker__teamleader__HeadOfDeportment__user=request.user,
		).order_by('date').all()
	head_of_deportment = HeadOfDeportment.objects.get(user=request.user)

	workers = Worker.objects.filter(teamleader__HeadOfDeportment__user=request.user).all()

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		teamleader = request.POST['teamleader']

		get_user = User.objects.get(username=teamleader)
		get_teamleader = TeamLeader.objects.get(user=get_user)

		user = User.objects.create_user(
			username=username, 
			password=password)
		user.save()

		user_profile = Profile(
			user=user, 
			group=0,
			)
		user_profile.save()

		new_worker = Worker(user=user, teamleader=get_teamleader)
		new_worker.save()

		return HttpResponseRedirect('/')

	template = 'create/create-worker.html'
	context = {
		'teamleaders': teamleaders_list,
		'data': get_data,
		'workers': workers,
	}
	return render(request, template, context)

@login_required
def change_teamleader(request, worker):
	teamleader = request.POST['teamleader']
	get_user_tl = User.objects.get(username=teamleader)
	get_user_worker = User.objects.get(username=worker)
	get_teamleader = TeamLeader.objects.get(user=get_user_tl)
	edit_worker = Worker.objects.get(user=get_user_worker)
	edit_worker.teamleader = get_teamleader
	edit_worker.save()
	return HttpResponseRedirect(f'/worker-statistics/{worker}/')

