from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
	title = models.CharField(max_length=250, default='', blank=True, null=True)
	body = models.TextField(default='', blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	image1 = models.ImageField(blank=True, upload_to='uploads/sketches/')
	caption1 = models.CharField(max_length=200, blank=True, null=True)
	image2 = models.ImageField(blank=True, upload_to='uploads/sketches/')
	caption2 = models.CharField(max_length=200, blank=True, null=True)
	image3 = models.ImageField(blank=True, upload_to='uploads/sketches/')
	caption3 = models.CharField(max_length=200, blank=True, null=True)
	image4 = models.ImageField(blank=True, upload_to='uploads/sketches/')
	caption4 = models.CharField(max_length=200, blank=True, null=True)
	is_published = models.BooleanField(default=False)

	def __str__(self):
		return self.title if self.title else 'Untitled'


	def snippet(self):
		return self.body[:50] + '...'

