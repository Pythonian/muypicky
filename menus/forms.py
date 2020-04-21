from django import forms
from .models import Item
from restaurants.models import Restaurant


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['restaurant', 'name', 'content',
					'exclude', 'public']


	def __init__(self, user=None, *args, **kwargs):
		super(ItemForm, self).__init__(*args, **kwargs)
		# Filter the restaurant list to show only those created by logged in user
		self.fields['restaurant'].queryset = Restaurant.objects.filter(owner=user).exclude(item__isnull=False)
		# def get_form_kwargs(self):
		# 	kwargs['user'] = self.request.user


