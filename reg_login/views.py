from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
	context = {}
	context.update(csrf(request))
	return render(request, 'log_reg/login.html', context)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/profile')
	else:
		return HttpResponseRedirect('/login')

def logout_view(request):
	return HttpResponseRedirect('/login')

def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login')
	
	context = {}
	context.update(csrf(request))
	context['form'] = UserCreationForm()

	return render(request,'log_reg/register.html', context)