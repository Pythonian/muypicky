from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.db.models import Q


User = settings.AUTH_USER_MODEL

class RestaurantQuerySet(models.query.QuerySet):
	'''
	<a href="{{ request.path }}?q={{ query }}">{{ query }}</a>
	'''
	def search(self, query): # Restaurant.objects.all().search(query)
		return self.filter(
			Q(name__icontains=query) |
			Q(location__icontains=query) |
			Q(category__icontains=query) |
			Q(item__name__icontains=query).distinct()
		)

class RestaurantManager(models.Manager):
	def get_queryset(self):
		return RestaurantQuerySet(self.model, using=self._db)

	def search(self, query): # Restaurant.objects.search()
		return self.get_queryset().search(query)


class Restaurant(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=120)
	slug = models.SlugField(max_length=50, unique=True)
	location = models.CharField(max_length=120,
		null=True, blank=True)
	category = models.CharField(max_length=120,
		null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = RestaurantManager()

	def __str__(self):
		return self.name


def restaurant_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

def restaurant_post_save_receiver(sender, instance, created, *args, **kwargs):
	pass

pre_save.connect(restaurant_pre_save_receiver, sender=Restaurant)

