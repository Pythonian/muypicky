from django.shortcuts import render, redirect

from .models import Profile


def follow_toggle(request):
	if request.method == 'POST':
		username_to_toggle = request.POST.get("username")
		profile_, is_following = Profile.objects.toggle_follow(request.user, username_to_toggle)
		# profile_ = Profile.objects.get(user__username__iexact=user_to_toggle)
		# user = request.user
		# if user in profile_.followers.all():
		# 	profile_.followers.remove(user)
		# else:
		# 	profile_.followers.add(user)
		return redirect(f"/u/{profile_.user.username}/")