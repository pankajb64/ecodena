# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, render
from django.contrib import auth
from django import forms
from Ecodena.User.models import *
from django.contrib.auth.views import login as auth_login
from Ecodena.User.views import generatePointsUser
from Ecodena.User.views import generateRank

def home(request):
	return render(request, 'index.html')
		


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		#profile = Profile.objects.filter(userID_f = request.user)
		#generatePointsUser(profile)
		
		#profile = Profile.objects.filter(userID_f = user)
		#profile[0].points_f = generatePointsUser(profile[0])
		#profile[0].rank_f = generateRank(profile[0])
		
		if user is not None and user.is_active:
			# Correct password, and the user is marked "active"
			
			profile = Profile.objects.filter(userID_f = user)[0]
			generatePointsUser(profile.userID_f)
			auth.login(request, user)
			profile.rank_f = generateRank(profile)
			profile.save()
			
			# Redirect to a success page.
			return HttpResponseRedirect("/")
		else:
			# Show an error page
			return auth.login(request, user)
	else:
		# Show an error page
		return render(request, 'registration/login.html')	

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
