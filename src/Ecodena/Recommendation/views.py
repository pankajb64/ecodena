from django.http import HttpResponse
from Recommendation.models import Recommendation
from django.shortcuts import render_to_response
from datetime import datetime
from django import forms
from django.template import RequestContext# Create your views here.
from Ecodena.Attempt.models import *
from Ecodena.Question.models import *


def viewRecommendations(request):
	if request.user.is_authenticated():
		recommendedquestions = generate_recommendations(request)
		return render_to_response('recommendations.html',{'recommendedQuestions':recommendedquestions})
	else:
		return HttpResponse("You need to log in first, only then can you access the url %s" %request.path)


def generate_recommendations(request):
	pass
	
	recommendation = Recommendation.objects.filter(userID_f = request.user)
	
	
	typesm = Attempt.objects.filter(userID_f = request.user).values('type').annotate(num_types=Count('type')).order_by('-num_types')[:3]

	
	t = (typesm[0].num_types + typesm[1].num_types + typesm[2].num_types)
	 
	t1 = round((typesm[0].num_types/t) * 50) 
	
	t2 = round((typesm[1].num_types/t) * 50)
	
	t3 = round((typesm[2].num_types/t) * 50 )
	
	levels_m = Attempt.objects.filter(userID_f = request.user).filter(questionID_f__in = Question.objects.filter(type_f = typesm[0].question.type_f)).filter(status_f = True ).distinct('questionID_f').annotate(num_levels=Count('level_f')).values('level_f').order_by('-num_levels')[:3]

	
	l_1 = (levels_m[0].num_types + levels_m[1].num_types + levels_m[2].num_types)
	l1 = round ((levels_m[0].num_types*levels_m[0].question.levelID_f) + (levels_m[1].num_types*levels_m[1].question.levelID_f) + (levels_m[2].num_types*levels_m[2].question.levelID_f))/l_1

	levels_m_2 = Attempt.objects.filter(userID_f = request.user).filter(questionID_f__in = Question.objects.filter(type_f = typesm[1].question.type_f)).filter(status_f = True ).distinct('questionID_f').annotate(num_levels=Count('level_f')).values('level_f').order_by('-num_levels')[:3]

	l_2 = (levels_m_2[0].num_types + levels_m_2[1].num_types + levels_m_2[2].num_types)
	l2 = round ((levels_m_2[0].num_types*levels_m_2[0].question.levelID_f) + (levels_m_2[1].num_types*levels_m_2[1].question.levelID_f) + (levels_m_2[2].num_types*levels_m_2[2].question.levelID_f))/l_2
	
	levels_m_3 = Attempt.objects.filter(userID_f = request.user).filter(questionID_f__in = Question.objects.filter(type_f = typesm[2].question.type_f)).filter(status_f = True ).distinct('questionID_f').annotate(num_levels=Count('level_f')).values('level_f').order_by('-num_levels')[:3]

	l_3 = (levels_m_3[0].num_types + levels_m_3[1].num_types + levels_m_3[2].num_types)
	l3 = round ((levels_m_3[0].num_types*levels_m_3[0].question.levelID_f) + (levels_m_3[1].num_types*levels_m_3[1].question.levelID_f) + (levels_m_3[2].num_types*levels_m_3[2].question.levelID_f))/l_3

	questions = Question.object.filter(type_f = typesm[0].question.type_f).filter(level_f = l1)

	recommendation.questionList_f[i].append(questions)
	
	'''for i in range [0,t1]:
		recommendation.questionList_f[i] = questions[i];'''

	questions = Question.object.filter(type_f = typesm[1].question.type_f).filter(level_f = l2)

	recommendation.questionList_f[i].append(questions)
	'''
	for i in range [(t1+1),(t1+t2)]:
		questionList_f[i] = questions[i];'''

	questions = Question.object.filter(type_f = typesm[1].question.type_f).filter(level_f = l3)
	
	recommendation.questionList_f[i].append(questions)
	'''
	for i in range [(t2+1),(t2+t3)]:
		questionList_f[i] = questions[i];  '''

	recommendation.save()
	
	return recommendation
	#(to be done by arun) object list_of_types[2] (order)
	
