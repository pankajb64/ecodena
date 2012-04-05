# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.contrib import auth
from django import forms

def home(request):
	return render(request, 'index.html')
		


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			# Correct password, and the user is marked "active"
			auth.login(request, user)
			# Redirect to a success page.
			return HttpResponseRedirect("/")
		else:
			# Show an error page
			return HttpResponseRedirect("/login/")
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
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", { 'form': form, })    

def sendmail(request):
	from django.core.mail import EmailMessage
	email = EmailMessage('Hello', 'World', to=['pankajb64@gmail.com'])
	email.send()
