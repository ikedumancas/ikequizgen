"""quizgen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^login/$', 'accounts.views.auth_login', name='login'),
    url(r'^logout/$', 'accounts.views.auth_logout', name='logout'),
    url(r'^changepassword/$', 'accounts.views.auth_changepassword', name='changepassword'),
    url(r'^edituser/$', 'accounts.views.auth_edituser', name='edituser'),
	url(r'^register/$', 'accounts.views.auth_register', name='register'),
    url(r'^quiz/', include('quizzes.urls', namespace="quizzes")),
    url(r'^admin/', include(admin.site.urls)),
]
