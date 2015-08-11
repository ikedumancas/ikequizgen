from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^dashboard/create/$', views.create_quiz, name='create_quiz'),
	url(r'^dashboard/(?P<id>[0-9]+)/$', views.quiz_dashboard, name='quiz_dashboard'),
	url(r'^dashboard/(?P<id>[0-9]+)/delete/$', views.quiz_delete, name='quiz_delete'),
]