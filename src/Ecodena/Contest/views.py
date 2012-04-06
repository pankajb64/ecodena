from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth.models import User
from Attempt.models import Attempt
from Question.models import Question
from User.models import Profile
from django.template import RequestContext 
from Contest.models import Contest
from Contest.models import ContestQuestion
from django import forms
import time
import datetime
from datetime import date
from Contest.models import ContestParticipants
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.decorators import login_required


class HoldContestForm(forms.Form):
	contestName = forms.CharField()
	contestpwd = forms.CharField(widget=forms.PasswordInput)
	contestpwd1 = forms.CharField(widget=forms.PasswordInput)	
	termsCond = forms.CharField(widget = forms.Textarea)
	contestFromDate = forms.DateField(widget = AdminDateWidget)
	contestToDate = forms.DateField(widget = AdminDateWidget)
	contestFromTime = forms.TimeField()
	contestToTime = forms.TimeField()
	def clean_password(self):
		if self.data['contestpwd'] != self.data['contestpwd1']:
			raise forms.ValidationError('Passwords are not the same')
		return self.data['contestpwd']
	
	def clean(self,*args, **kwargs):
		#self.clean_email()
		self.clean_password()
		return super(HoldContestForm, self).clean(*args, **kwargs)
	

@csrf_protect	
@login_required(login_url="/login/")
def holdContest(request):
	
	f=HoldContestForm()
	dc = {'form':f}
	context = RequestContext(request, dc)
	if request.method == "POST":
		f=HoldContestForm(request.POST)
		if not f.is_valid():
			dc = {'form':f}
			context = RequestContext(request, dc)
			#raise Http404
			return render_to_response('holdContest.html',context)
		else:
			contest=Contest()
			context = RequestContext(request,dc)
		#	contest.adminID = User.objects.filter(User.username="sen3")[0]
			contest.contestName_f = f.cleaned_data['contestName']
			contest.contestpwd_f = f.cleaned_data['contestpwd']
			contest.termsCond = f.cleaned_data['termsCond']
			contest.contestFromDate = f.cleaned_data['contestFromDate']
			contest.contestToDate = f.cleaned_data['contestToDate']
			contest.contestFromTime = f.cleaned_data['contestFromTime']
			contest.contestToTime = f.cleaned_data['contestToTime']
			#contest.isApproved = False
			contest.save()
			f=HoldContestForm()
			#contestID = contest.contestID
			
			return HttpResponse("Your contest is send to admin for approval%s"%request.path)
	else:
		return render_to_response('holdContest.html',context)
	
def listContests(request):
	contest = Contest.objects.filter(contestToDate_f__gte=datetime.datetime.now().date()).filter(contestToTime_f__gte=datetime.datetime.now().time())
	return render_to_response('listContests.html',{'contest':contest,'time':datetime.datetime.now().time(),'date':datetime.datetime.now()})
	
	
	
def registerInContest(request,contestID):
	cp = ContestParticipants()
	cp.contestID = contestID
	cp.userID = request.userID
	cp.save()
	return render_to_response('registeredSuccessfully.html',{'cp':cp})
	
def contestCompleted(request):
	cp = ContestParticipants.objects.filter(userID=request.user)[0]
	if cp:
		contest = Contest.objects.filter(contestToDate__lte=datetime.now().date()).filter(contestToTime__lt=datetime.time(datetime.now()))
		return contest
	else:
		return None
	
	
def participateInContestlist(request):
	cp = ContestParticipants.objects.filter(userID=request.user)[0]
	if cp:
		completedContest = contestCompleted()
		contest = Contest.objects.filter(contestFromDate__lte=datetime.now().date()).filter(contestToDate__gte=datetime.now().date()).filter(contestFromTime__lte=datetime.time(datetime.now())).filter(contestToTime__gte=datetime.time(datetime.now()))
		return render_to_response('listparticipated.html',{'contest':contest,'completedContest':completedContest})

def retrieveScore(request,cID):
	pass
	'''questions = ContestQuestion.objects.filter(contestID=cID)
	contest = Contest.objects.filter(contestID=cID)
	return render_to_response('contestQuestions.html',{'questions':questions,'contest':contest})'''	
	
def listScore(request,cID):
	#score = ContestParticipants.objects.filter(contestID=cID).order_by(score)
	contestPart = ContestParticipants.objects.filter(contestID=cID).order_by(score)
	#uID = User.objects.filter(userID)
	contest=Contest.objects.filter(contestID=cID)[0]
	return render_to_response('listScore.html',{'contest':contest,'contestPart':contestPart})
	
def listContestQuestion(request,contestID):
	'''list all the questions with its title
	parameter:request-->All the details associated with URL 
	returns the question.html webpage and the list of questions'''
	questions =ContestQuestion.objects.filter(contestID_f=contestID)
	contest = Contest.objects.filter(contestID_f=contestID)[0]
	return render_to_response('contestQuestions.html',{'questions':questions,'contest':contest})
	
def contestQuestion(request,contestID,questionID):
	question = ContestQuestion.objects.filter(questionID_f=questionID)[0]
	contest = Contest.objects.filter(contestID_f=contestID)[0]
	return render_to_response('contestQuestion.html',{'question':question,'contest':contest})
	

	




	
					
				
