from django.db import models
from django.conf import settings
from restaurants.models import Restaurant


class Item(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL)
	restaurant = models.ForeignKey(
		Restaurant)
	name = models.CharField(
		max_length=120)
	content = models.TextField(
		help_text='Separate each item by comma')
	exclude = models.TextField(
		blank=True,
		null=True)
	public = models.BooleanField(
		default=True)
	timestamp = models.DateTimeField(
		auto_now_add=True)

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.name

	def get_contents(self):
		# Return the content in a list and separate by comma
		return self.content.split(",")

	def get_excludes(self):
		return self.exclude.split(",")