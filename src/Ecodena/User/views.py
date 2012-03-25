# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from Attempt.models import Attempt
from Question.models import Question
from User.models import Profile
from django.template import RequestContent 



class ProfileForm(forms.Form):
	username = forms.CharField()
	dob = forms.DateField()
	GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
	)
	gender=forms.ChoiceField(choices=GENDER_CHOICES)
	email=forms.EmailField()
	address  = forms.CharField(widget=forms.Textarea)
	
	
def viewProfile(request):
	if request.user.is_authenticated():
		profile = User.objects.filter(UserID_f=request.user)
		p=Profile.objects.filter(UserID_f=request.user)[0]
		a=Attempt.objects.filter(UserID_f=request.user).orderby(timeOfSubmission):5
		countAttempt = Attempt.objects.filter(UserID_f=request.user).count()
		countCorrect = Attempt.objects.filter(UserID_f=request.user).filter(status=True).count()
		countIncorrect = countAttempt-countCorrect
		email=profile.email
		
		dc = {'userName':request.user.username , 'dob':p.dob_f, 'gender':p.gender_f,'email':email, 'address':p.address_f,'title':a.questionID_f,'countAttempt':countAttempt,'countCorrect':countCorrect,'countIncorrect':countIncorrect}
		if profile:
			profile=profile[0]
		return render_to_response('profile.html',dc)
	else:
		return HttpResponse("You need to log in to view your profile %s" %request.path)
			
		
#def viewsProfileByID(request,profileID)
def editProfile(request)
	if request.user.is_authenticated():
		f=ProfileForm()
		context = RequestContext(request, {'form':f})
		profile = User.objects.filter(UserID_f=request.user)
		p=Profile.objects.filter(UserID_f=request.user)[0]
		a=Attempt.objects.filter(UserID_f=request.user).orderby(timeOfSubmission):5
		countAttempt = Attempt.objects.filter(UserID_f=request.user).count()
		countCorrect = Attempt.objects.filter(UserID_f=request.user).filter(status=True).count()
		countIncorrect = countAttempt-countCorrect
		email=profile.email
		
		dc = {'userName':request.user.username , 'profile':profile,'email':email,'title':a.questionID_f,'countAttempt':countAttempt,'countCorrect':countCorrect,'countIncorrect':countIncorrect}
		if request.method =="POST":
			f=ProfileForm(request.POST)
			if not f.is_valid():
				return render_to_response('editProfile.html', context)
			else:
				 = Profile()
				dc = { ,'dt':dt}
				context = RequestContext(request, dc)
				profile.dob = f.dob
				profile.address = f.address
				profile.gender = f.gender
				profile.save()
				
				return render_to_response('editProfile.html', context) 
			
			#language = Language.objects.all()
			
		return render_to_response('editProfile.html',context)

		
	

