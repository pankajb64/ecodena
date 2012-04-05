from django.contrib.auth.models import User
from Question.models import Question



from django.db import models


# Create your models here.

class ProblemSetter(User,object):
	pass
		

class HasSet(models.Model,object):
	questionID_f = models.ForeignKey(Question,verbose_name="QuestionID of the Question", null=False,unique=True)
	userID_f = models.ForeignKey(User,verbose_name="UserID of the setter of the particular Question",null=False,unique=False)
	
	def getQuestionID(self):
		return self.questionID_f
	def setQuestionID(self,queID):
		self.questionID_f = queID
		 
	questionID = property(getQuestionID,setQuestionID)
	
	def getUserID(self):
		return self.userID_f
	def setUserID(self,uID):
		self.userID_f = uID
	
	userID = property(getUserID,setUserID)	
	
	class Meta:
		verbose_name = 'Question UserID'
		verbose_name_plural = 'Question UserIDs'
	def __unicode__(self):
		return `self.questionID`+' '+`self.userID`
