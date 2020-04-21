from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Restaurant
from .forms import RestaurantForm 

def restaurant_list(request):

	query = request.GET.get('q')
	qs = Restaurant.objects.filter(owner=user)
	if query:
		# Search within a User restaurant list
		qs = qs.search(query)
		# qs = qs.filter(name__icontains=query)

	template = 'restaurants/list.html'
	context = {}

	return render(request, template, context)


@login_required
def restaurant_form(request):

	form = RestaurantForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.owner = request.user
		instance.save()
		return redirect('detail')

	template = 'restaurants/form.html'
	context = {
		'form': form,
	}

	return render(request, template, context)