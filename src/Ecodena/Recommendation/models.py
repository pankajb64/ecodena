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
