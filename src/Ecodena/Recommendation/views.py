from django.http import HttpResponse
from Recommendation.models import Recommendation
from django.shortcuts import render_to_response
from datetime import datetime
from django import forms
from django.template import RequestContext# Create your views here.



def viewRecommendations(request):
	if request.user.is_authenticated():
		recommendedquestions=Recommendation.objects.filter(userID_f=request.user)[0]
		return render_to_response('recommendations.html',{'recommendedQuestions':recommendedquestions})
	else:
		return HttpResponse("You need to log in first, only then can you access the url %s" %request.path)

	
