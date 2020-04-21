import random
import string
from django.utils.text import slugify

RESERVED_SLUGS = ['create']

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
	'''
	This is for a Django project and it assumes that
	your instance has a model with a slug and name field.
	'''
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.name)

	if slug in RESERVED_SLUGS:
		new_slug = "{slug}-{randstr}".format(
			slug=slug,
			randstr=random_string_generator(size=4)
		)		
		return unique_slug_generator(instance, new_slug=new_slug)

	Klass = instance.__class__
	qs_exists = Klass.objects.filter(slug=slug).exists()
	if qs_exists:
		new_slug = "{slug}-{randstr}".format(
			slug=slug,
			randstr=random_string_generator(size=4)
		)
		return unique_slug_generator(instance, new_slug=new_slug)
	return slug