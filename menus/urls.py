from django.conf.urls import url 
from . import views


urlpatterns = [

	url(r'^$',
		views.list_view,
		name='list'),

	url(r'^create/$',
		views.list_view,
		name='list'),

	url(r'^(?P<pk>\d+)/$',
		views.detail_view,
		name='detail'),	

]