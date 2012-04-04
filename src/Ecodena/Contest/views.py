# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
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



class HoldContestForm(forms.Form):
	contestName = forms.CharField()
	contestpwd = forms.CharField()
	termsCond = forms.CharField(widget = forms.Textarea)
	contestFromDate = forms.DateField()
	contestToDate = forms.DateField()
	contestFromTime = forms.TimeField()
	contestToTime = forms.TimeField()

@csrf_protect	
def holdContest(request):
	if request.user.is_authenticated():
		f=HoldContestForm()
		dc = {'form':f}
		context = RequestContext(request, dc)
		if request.method == "POST":
			f=HoldContestForm(request.POST)
			if not f.is_valid():
				return render_to_response('holdContest.html',context)
			else:
				contest=Contest()
				dc = {'contestID':contestID}
				context = RequestContext(request,dc)
				contest.contestName_f = f.contestName
				contest.contestpwd_f = f.contestpwd
				contest.termsCond = f.termsCond
				contest.contestFromDate = f.contestFromDate
				contest.contestToDate = f.contestToDate
				contest.contestFromTime = f.contestFromTime
				contest.contestToTime = f.contestToTime
				contest.save()
				contestID = contest.contestID
				
				return render_to_response('holdContest.html',context)
		else:
			return render_to_response('holdContest.html',context)
	else:
		return HttpResponse("You need to log in to hold contest %s"%request.path)					

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
	

	




	
					
				
