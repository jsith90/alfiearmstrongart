from django.db import models
import datetime


class Gallery(models.Model):
	title = models.CharField(max_length=250, default='', blank=True, null=True)
	description = models.TextField(max_length=500, default='', blank=True, null=True)
	is_published = models.BooleanField(default=False)

	def __str__(self):
		return self.title if self.title else 'Untitled'

	class Meta:
		verbose_name_plural = 'galleries'

class Image(models.Model):
	gallery = models.ForeignKey(Gallery, related_name='image', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='uploads/works/')
	caption = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return f'Image {self.id}'
