from django.conf.urls import urls
from rango import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	]