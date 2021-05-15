
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


GROUP = ((0, 'worker'), (1, 'teamleader'), (2, 'head_of_deportment'))

#superuser is created by python manage.py createsuperuser command
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	group = models.SmallIntegerField(choices=GROUP)
	image = models.ImageField(upload_to='profile/worker/image', blank=True)

class HeadOfDeportment(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='head_of_deportment')

	def __str__(self):
		return self.user.username

class TeamLeader(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_temaleader', blank=True, null=True)
	HeadOfDeportment = models.ForeignKey(HeadOfDeportment, on_delete=models.CASCADE, related_name='head_of_deportment', blank=True, null=True)

	def get_temaleader_url(self):
		return reverse('teamleader-statistics',
						args=[self.user.username])

class Worker(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker')
	teamleader = models.ForeignKey(TeamLeader, on_delete=models.CASCADE, related_name='teamleader')

	def get_worker_url(self):
		return reverse('worker-statistics',
						args=[self.user.username])

class TestData(models.Model):
	'''data table'''
	worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='worker')
	data1 = models.IntegerField()
	data2 = models.IntegerField()
	data3 = models.IntegerField()
	data4 = models.IntegerField()
	data5 = models.IntegerField()
	date = models.DateField()

	class Meta:
		verbose_name = 'data' 
		verbose_name_plural = 'data'

	def __str__(self):
		return (f'{self.worker.user.username} - {self.date}')