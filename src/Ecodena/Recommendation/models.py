from django.db import models
from django.contrib.auth.models import User
from Ecodena.Question.models import Question
from Ecodena.Attempt.models import Attempt
import datetime
from django.db.models import Count
import math

# Create your models here.

class Recommendation(models.Model):

	userID_f = models.ForeignKey(User, verbose_name="UserID", null=False, related_name='+' )
	#questionList_f = models.ManyToManyField(Question)
	questionList_f = models.CommaSeparatedIntegerField("The list of question Ids recommended",max_length = 20 ,null = False )

def generate_recommendations(self):
	
	typesm = Attempt.objects.filter(attempt.userID.userID = self.userID_f).values('type').annotate(num_types=Count('type')).order_by('-num_types')[:3]

	
	t = (typesm[0].num_types + typesm[1].num_types + typesm[2].num_types)
	 
	t1 = round((typesm[0].num_types/t) * 50) 
	
	t2 = round((typesm[1].num_types/t) * 50)
	
	t3 = round((typesm[2].num_types/t) * 50 )
	
	levels_m = Attempt.objects.filter(attempt.userID.userID = self.userID).filter(attempt.question.type = typesm[0].question.type).filter(attempt.status = True ).annotate(num_levels=Count('level')).values('level').order_by('-num_levels')[:3]

	l_1 = (levels_m[0].num_types + levels_m[1].num_types + levels_m[2].num_types)
	l1 = ((levels_m[0].num_types*levels_m[0].question.levelID_f) + (levels_m[1].num_types*levels_m[1].question.levelID_f) + (levels_m[2].num_types*levels_m[2].question.levelID_f))/l_1

	levels_m_2 = Attempt.objects.filter(attempt.userID.userID = self.userID).filter(attempt.question.type = typesm[1].question.type).filter(attempt.status = True ).annotate(num_levels=Count('level')).values('level').order_by('-num_levels')[:3]

	l_2 = (levels_m_2[0].num_types + levels_m_2[1].num_types + levels_m_2[2].num_types)
	l2 = ((levels_m_2[0].num_types*levels_m_2[0].question.levelID_f) + (levels_m_2[1].num_types*levels_m_2[1].question.levelID_f) + (levels_m_2[2].num_types*levels_m_2[2].question.levelID_f))/l_2
	
	levels_m_3 = Attempt.objects.filter(attempt.userID.userID = self.userID).filter(attempt.question.type = typesm[2].question.type).filter(attempt.status = True ).annotate(num_levels=Count('level')).values('level').order_by('-num_levels')[:3]

	l_3 = (levels_m_3[0].num_types + levels_m_3[1].num_types + levels_m_3[2].num_types)
	l3 = ((levels_m_3[0].num_types*levels_m_3[0].question.levelID_f) + (levels_m_3[1].num_types*levels_m_3[1].question.levelID_f) + (levels_m_3[2].num_types*levels_m_3[2].question.levelID_f))/l_3

	questions = Question.object.filter(question.type = typesm[0].question.type).filter(question.level = l1)

	for i in range [0,t1]:
		questionList_f[i] = questions[i];

	questions = Question.object.filter(question.type = typesm[1].question.type).filter(question.level = l2)

	for i in range [(t1+1),(t1+t2)]:
		questionList_f[i] = questions[i];

	questions = Question.object.filter(question.type = typesm[2].question.type).filter(question.level = l3)

	for i in range [(t2+1),(t2+t3)]:
		questionList_f[i] = questions[i];  
  

	#(to be done by arun) object list_of_types[2] (order)

