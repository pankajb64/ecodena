# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.contrib.auth.models import User
from Attempt.models import Attempt
from Question.models import Question
from User.models import Profile
from django import forms
from django.template import RequestContext 
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.forms.formsets import formset_factory


class ProfileForm(forms.Form):
	dob = forms.DateField()
	GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
	)
	gender=forms.ChoiceField(choices=GENDER_CHOICES,required=False)
	email=forms.EmailField(required=False)
	address  = forms.CharField(widget=forms.Textarea,required=False)
	
	
def viewProfile(request):
	if request.user.is_authenticated():
		profile = User.objects.filter(username=request.user.username)[0]
		p=Profile.objects.filter(userID_f=request.user)[0]
		a=Attempt.objects.filter(userID_f=request.user).order_by('timeOfSubmission_f')
		countAttempt = Attempt.objects.filter(userID_f=request.user).count()
		countCorrect = Attempt.objects.filter(userID_f=request.user).filter(status_f=True).count()
		countIncorrect = countAttempt-countCorrect
		email=profile.email
		
		dc = {'user':request.user , 'p':p,'a':a,'countAttempt':countAttempt,'countCorrect':countCorrect,'countIncorrect':countIncorrect}
		if profile:
			return render('profile.html',dc)
	else:
		return HttpResponse("You need to log in to view your profile %s" %request.path)
			
			
def viewProfileByID(request,profileID):
	
	p=Profile.objects.filter(profileID_f=profileID)[0]
	
	
	a=Attempt.objects.filter(userID_f=profileID).order_by('timeOfSubmission_f')
	countAttempt = Attempt.objects.filter(userID_f=profileID).count()
	countCorrect = Attempt.objects.filter(userID_f=profileID).filter(status_f=True).count()
	countIncorrect = countAttempt-countCorrect
	dc = {'profile':p, 'attempt':a,'countAttempt':countAttempt,'countCorrect':countCorrect,'countIncorrect':countIncorrect}
	if p:
		return render('profileID.html',dc)	
	else:
		return HttpResponse("Fuck U!!!%s"%request.path)
@csrf_protect	
def editProfile(request):
	if request.user.is_authenticated():
		f=ProfileForm()
		ProfileFormSet = formset_factory(ProfileForm)
		p=Profile.objects.filter(userID_f=request.user)[0]
		u = request.user
		dc = {'form':f,'profile':p,'user':request.user}
		context = RequestContext(request,dc)
		
		if request.method =="POST":
			f=ProfileForm(request.POST)
			if not f.is_valid():
				return render_to_response('editProfile.html', context)
			else:
				#profile = Profile()
				#profile.profileID_f = p.profileID_f
				dc = {'form':f,'profile':p,'user':request.user}
				context = RequestContext(request, dc)
			#	p = f.save()
				if f.dob:
					p.dob_f = f.dob
				if f.address:
					p.address_f = f.address
				if f.gender:	
					p.gender_f = f.gender
				if f.email:
					u.email = f.email
				p.save()
				u.save()
				
				
				return render('editProfile.html', context) 
			
			#language = Language.objects.all()
			
		return render('editProfile.html',context)

		
	


