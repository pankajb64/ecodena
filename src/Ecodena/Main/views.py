# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, render
from django.contrib import auth
from django import forms
from Ecodena.User.models import *
from django.contrib.auth.views import login as auth_login

def home(request):
	return render(request, 'index.html')
		


def login(request):
	if not request.user.is_authenticated():
		return auth_login(request,)	
	else:
		return HttpResponseRedirect("/profile/")		

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")
    
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	email=forms.EmailField()
	first_name = forms.CharField() 
	last_name = forms.CharField() 

def register(request):
	if not request.user.is_authenticated():
		
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				new_user = form.save()
				new_user.email = form.cleaned_data['email']
				new_user.first_name = form.cleaned_data['first_name']
				new_user.last_name = form.cleaned_data['last_name']
				new_user.save()
				profile = Profile()
				profile.userID_f = new_user
				profile.save()
				return render(request, "registration_complete.html")
		else:
			form = RegisterForm()
		return render(request, "registration/register.html", { 'form': form, })    
	else:
		return HttpResponseRedirect("/profile/")	

def sendmail(request):
	from django.core.mail import EmailMessage
	email = EmailMessage('Hello', 'World', to=['pankajb64@gmail.com'])
	email.send()
	#raise Http404
