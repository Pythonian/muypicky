from django.shortcuts import render
from .models import Item
from .forms import ItemForm


def item_list(request):
	item_list = Item.objects.filter(user=request.user)

	# Get the User id's of people the requested user follows
	user = request.user
	is_following_user_ids = [x.user.id for x in user.is_following.all()]
	# Get the items based of the returned user id's
	qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True)

	return render(request, template, context)


def item_create(request):
	form = ItemForm(request.POST or None)


	