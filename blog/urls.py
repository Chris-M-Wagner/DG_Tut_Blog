# mysite/urls.py refers to this document to direct url traffic.

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]

