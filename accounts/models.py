from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
	def toggle_follow(self, requested_user, username_to_toggle):
		profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
		user = requested_user
		is_following = False
		if user in profile_.followers.all():
			profile_.followers.remove(user)
		else:
			profile_.followers.add(user)
			is_following = True
		return profile_, is_following


class Profile(models.Model):
	user = models.OneToOneField(
		User)
	followers = models.ManyToManyField(
		User,
		related_name='followers',
		blank=True)
	following = models.ManyToManyField(
		User,
		related_name='following',
		blank=True)
	created = models.DateTimeField(
		auto_now_add=True)
	activated = models.BooleanField(
		default=False)

	objects = ProfileManager()

	def __str__(self):
		return self.user

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		profile, is_created = Profile.objects.get_or_create(user=instance)
		# Add the newly created profile to a list of followers for a User
		default_user_profile = Profile.objects.get(user__id=1)
		default_user_profile.followers.add(instance)
		# Add a User to the followers list of a newly created profile
		profile.followers.add(default_user_profile.user)

post_save.connect(post_save_user_receiver, sender=User)
