from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm,UserCreationForm

from .forms import UserCreateForm


def auth_login(request):
	if request.user.is_authenticated():
		return redirect('quizzes:dashboard')
	form = AuthenticationForm(data=request.POST or None)
	next_url = request.GET.get('next')
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username,password=password)
		login(request,user)
		if next_url:
			return HttpResponseRedirect(next_url)	
		return redirect('quizzes:dashboard')
	context = {
		'form':form
	}
	template = "login.html"
	return render(request, template, context)


@login_required
def auth_logout(request):
	logout(request)
	return redirect('login')


@login_required
def auth_changepassword(request):
	form = PasswordChangeForm(request.POST or None)
	context = {
		'form':form
	}
	template = "changepassword.html"
	return render(request, template, context)


@login_required
def auth_edituser(request):
	form = UserChangeForm(instance=request.user)
	context = {
		'form':form
	}
	template = "userform.html"
	return render(request, template, context)


def auth_register(request):
	if request.user.is_authenticated():
		return redirect('quizzes:dashboard')
	form = UserCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request,'<strong>Account created!</strong>  You can now login to your account.')
		return redirect('login')
	context = {
		'form':form
	}
	template = "register.html"
	return render(request, template, context)