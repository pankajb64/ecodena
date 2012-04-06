# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
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
from django.contrib.auth.decorators import login_required

class ProfileForm(forms.Form):
	dob = forms.DateField(required=False)
	GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
	)
	gender=forms.ChoiceField(choices=GENDER_CHOICES,required=False)
	email=forms.EmailField(required=False)
	address  = forms.CharField(widget=forms.Textarea,required=False)
	
@login_required(login_url="/login/")	
def viewProfile(request):
	profile=Profile.objects.filter(userID_f=request.user)[0]
	a = Attempt.objects.filter(userID_f=request.user)
	attempts = a.order_by('timeOfSubmission_f')
	countAttempt = a.count()
	countCorrect = a.filter(status_f=True).count()
	countCompileError = a.filter(errorReportID_f__errorType_f = 1).count()
	countRunTimeError = a.filter(errorReportID_f__errorType_f = 2).count()
	countTimeLimitExceeded = a.filter(errorReportID_f__errorType_f = 3).count()
	countMemoryLimitExceeded = a.filter(errorReportID_f__errorType_f = 4).count()
	countWrongAnswer = a.filter(errorReportID_f__errorType_f = 5).count()
	
	#dc = { 'p':p,'attempts':a,'countAttempt':countAttempt,'countCorrect':countCorrect,'countIncorrect':countIncorrect}
	return render(request, 'profile.html',locals())


def viewProfileByID(request,username):
	
	targetuser = User.objects.filter(username=username)
	
	profile=Profile.objects.filter(userID_f=targetuser)
	
	if profile:
		profile=profile[0]
		a = Attempt.objects.filter(userID_f=request.user)
		attempts = a.order_by('timeOfSubmission_f')
		countAttempt = a.count()
		countCorrect = a.filter(status_f=True).count()
		countCompileError = a.filter(errorReportID_f__errorType_f = 1).count()
		countRunTimeError = a.filter(errorReportID_f__errorType_f = 2).count()
		countTimeLimitExceeded = a.filter(errorReportID_f__errorType_f = 3).count()
		countMemoryLimitExceeded = a.filter(errorReportID_f__errorType_f = 4).count()
		countWrongAnswer = a.filter(errorReportID_f__errorType_f = 5).count()

		#dc = { 'p':p,'attempts':a,'countAttempt':countAttempt,'countCorrect':countCorrect,'countIncorrect':countIncorrect}
		return render(request, 'profile.html',locals())
	else:
		return HttpResponseRedirect("/profile")	
@csrf_protect	
def editProfile(request):
	if request.user.is_authenticated():
		f=ProfileForm()
		p=Profile.objects.filter(userID_f=request.user)[0]
		u = request.user
		dc = {'form':f,'profile':p,'user':request.user}
		context = RequestContext(request,dc)
		
		if request.method =="POST":
			f=ProfileForm(request.POST)
			if not f.is_valid():
				return render(request,'editProfile.html', context)
			else:
				#profile = Profile()
				#profile.profileID_f = p.profileID_f
				dc = {'form':f,'profile':p,'user':request.user}
				context = RequestContext(request, dc)
			#	p = f.save()
				if f.cleaned_data['dob']: 
					p.dob_f = f.cleaned_data['dob']	
				if f.cleaned_data['address']: 			
					p.address_f = f.cleaned_data['address']	
				if f.cleaned_data['gender']:				
					p.gender_f = f.cleaned_data['gender']	
				if f.cleaned_data['email']:			
					u.email = f.cleaned_data['email']
				p.save()
				u.save()
				
				
				return HttpResponseRedirect('/profile')
			
			#language = Language.objects.all()
			
		return render(request,'editProfile.html',context)
	return HttpResponse("Fuck Off!!%s"%request.path)

def generatePointsUser(request):
	
	basepoints = 1500
	points_f = basepoints
	n = Attempt.objects.filter(userID = request.userID_f).distinct('questionID_f').filter(status = True).count()	
	attempts_c = Attempt.objects.filter(userID = request.userID_f).distinct('questionID_f').filter(status = True)	
	
	for i in range[0,n]:
		points_f = points_f + (attempt_c[i].questionID_f.questionRating_f * 10)
		 
	m = Attempt.objects.filter(userID = request.userID_f).filter(status = False).count()	
	attempts_w =  Attempt.objects.filter(userID = request.userID_f).filter(status = False).
	
	for j in range[0,m]:
		points_f = points_f - (10/(attempt_w[j].questionID_f.questionRating_f))
	
	return points_f	
		
def generateRank(request):
	
	ranking = User.objects.order_by('-points_f')
	n = User.objects.order_by('-points_f').count()
	
	for i in range[0,n]:
		if ranking[i].userID == request.userID_f:
			rank_f = i
	
	return rank_f
