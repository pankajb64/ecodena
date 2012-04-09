from django.http import HttpResponse
from Recommendation.models import Recommendation
from django.shortcuts import render_to_response,render
from datetime import datetime
from django import forms
from django.template import RequestContext# Create your views here.
from Ecodena.Attempt.models import *
from Ecodena.Question.models import *
import datetime
from django.db.models import Count
import math
from django.template import Library
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/login/')
def viewRecommendations(request):
	
	recommendedquestions = Recommendation.objects.filter(userID_f = request.user)
	
	if not recommendedquestions :
		recommendedquestions = generate_recommendations(request)
	else:
		recommendedquestions = recommendedquestions[0]	
	return render(request,'recommendations.html',{'recommendedQuestions':recommendedquestions})
	


def generate_recommendations(request):
	
	
	recommendation = Recommendation.objects.filter(userID_f = request.user)
	
	if recommendation:
		recommendation = recommendation[0]
		recommendation.delete()
		
	recommendation = Recommendation()
	recommendation.userID_f = request.user
	recommendation.save()
			
	from django.db import connection, transaction
	cursor = connection.cursor()

    # Data retrieval operation - no commit required
    #cursor.execute("SELECT typeID_f, COUNT(Distinct Q.questionID_f) AS num_types FROM Attempt_attempt AS A, Question_question AS Q, Question_type AS T	WHERE A.userID_f_id == %s AND A.questionID_f_id == Q.questionID_f AND Q.typeID_f_id == T.typeID_f GROUP BY T.typeID_f" , [request.user.username])
    #dictfetchall(cursor)
    
    #return row
	#sql = "SELECT typeID_f, COUNT(Distinct Q.questionID_f) AS num_types FROM Attempt_attempt AS A, Question_question AS Q, Question_type AS T	WHERE A.userID_f_id == %s AND A.questionID_f_id == Q.questionID_f AND Q.typeID_f_id == T.typeID_f GROUP BY T.typeID_f" , [request.user.username]
	
	t= Attempt.objects.filter(userID_f = request.user).distinct('questionID_f__type_f__typeID_f').annotate(num = Count('questionID_f__type_f__typeID_f'))

	
	if not t  :
		
		questions = Question.objects.filter(level_f__levelID_f = '1').exclude(questionID_f__in = Attempt.objects.filter(userID_f = request.user)  )
		
		for question in questions:
			
			recommended = Recommended()
			recommended.question = question
			recommended.recommendation = recommendation
			recommended.save()
		return recommendation
		

	elif t[0].num < 3:
		
		attempt_m = Attempt.objects.annotate(nums =Count('questionID_f__type_f__typeID_f')).order_by('-nums')[:2]
		questions = Question.objects.filter(type_f = attempt_m[0].questionID_f.type_f).filter(level_f__levelID_f = '1').exclude(questionID_f__in = Attempt.objects.filter(userID_f = request.user)  ) 
		
		recommendation.questionList_f[i].append(questions)
		recommendation.save()
		return recommendation[0]
		
 
		
	else:
		typesm = Attempt.objects.filter(userID_f = request.user).annotate(num_types=Count('questionID_f__type_f__typeID_f')).order_by('-num_types')[:3]

		t = (typesm[0].num_types + typesm[1].num_types + typesm[2].num_types)
	 
		t1 = round((typesm[0].num_types/t) * 10) 
	
		t2 = round((typesm[1].num_types/t) * 10)
		
		t3 = round((typesm[2].num_types/t) * 10 )
		
		levels_m = Attempt.objects.filter(userID_f = request.user).filter(questionID_f__in = Question.objects.filter(type_f = typesm[0].question.type_f)).filter(status_f = True ).distinct('questionID_f').annotate(num_levels=Count('level_f')).values('level_f').order_by('-num_levels')[:3]

		
		l_1 = (levels_m[0].num_types + levels_m[1].num_types + levels_m[2].num_types)
		l1 = round ((levels_m[0].num_types*levels_m[0].question.levelID_f) + (levels_m[1].num_types*levels_m[1].question.levelID_f) + (levels_m[2].num_types*levels_m[2].question.levelID_f))/l_1

		levels_m_2 = Attempt.objects.filter(userID_f = request.user).filter(questionID_f__in = Question.objects.filter(type_f = typesm[1].question.type_f)).filter(status_f = True ).distinct('questionID_f').annotate(num_levels=Count('level_f')).values('level_f').order_by('-num_levels')[:3]

		l_2 = (levels_m_2[0].num_types + levels_m_2[1].num_types + levels_m_2[2].num_types)
		l2 = round ((levels_m_2[0].num_types*levels_m_2[0].question.levelID_f) + (levels_m_2[1].num_types*levels_m_2[1].question.levelID_f) + (levels_m_2[2].num_types*levels_m_2[2].question.levelID_f))/l_2
		
		levels_m_3 = Attempt.objects.filter(userID_f = request.user).filter(questionID_f__in = Question.objects.filter(type_f = typesm[2].question.type_f)).filter(status_f = True ).distinct('questionID_f').annotate(num_levels=Count('level_f')).values('level_f').order_by('-num_levels')[:3]

		l_3 = (levels_m_3[0].num_types + levels_m_3[1].num_types + levels_m_3[2].num_types)
		l3 = round ((levels_m_3[0].num_types*levels_m_3[0].question.levelID_f) + (levels_m_3[1].num_types*levels_m_3[1].question.levelID_f) + (levels_m_3[2].num_types*levels_m_3[2].question.levelID_f))/l_3

		questions = Question.objects.filter(type_f = typesm[0].question.type_f).filter(level_f = l1).exclude(questionID_f__in = Attempt.objects.filter(userID_f = request.user)  )

		recommendation[0].questionList_f[i].append(questions)
		
		
		

		questions = Question.objects.filter(type_f = typesm[1].question.type_f).filter(level_f = l2).exclude(questionID_f__in = Attempt.objects.filter(userID_f = request.user)  )

		recommendation[0].questionList_f[i].append(questions)
		

		questions = Question.objects.filter(type_f = typesm[1].question.type_f).filter(level_f = l3).exclude(questionID_f__in = Attempt.objects.filter(userID_f = request.user)  )
		
		recommendation[0].questionList_f[i].append(questions)
		
		recommendation[0].save()
		
		return recommendation[0]
	
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
