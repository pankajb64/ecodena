from django.db import models
from Ecodena.User.models import User
from Ecodena.Question.models import Question
import datetime

# Create your models here.

class Comment(models.Model):
	commentID = models.AutoField(primary_key=True)
	commentText = models.TextField("The Body of the Comment", null=False)
	isReported = models.BooleanField("Is the comment Reported ?", default=False)
	userID = models.ForeignKey(User, verbose_name="User ID", null=False, related_name='+')
	reportingUserID =  models.ForeignKey(User, verbose_name="User ID of the user who reported this comment", related_name='+')
	questionID = models.ForeignKey(Question, verbose_name="Question ID", null=False)
	timeStamp = models.DateTimeField("Time of Posting", null=False)


	def getCommentText(self):
		return self.__commentText
	def setCommentText(self, comment):
		self.__commentText = comment
	commentText = property(getCommentText, setCommentText)

	
	
	def getTimeStamp(self):
		return self.__timeStamp
	def setTimeStamp(self, Timestamp):
		self.__timeStamp = Timeastamp
	timeStamp = property(getTimeStamp, setTimeStamp)

	

	def isReported(self):
		return isReported

		
	def report(self, status):
		self.__isReported = status
	
	

	def getUserID(self):
		return self.__UserID 
	def setUserID(self, uID):
		self.__UserID = uID
	UserID = property(getUserID, setUserID)	
	

	def getReportingUserID(self):
		return self.__reportingUserID
	def setReportingUserID(self, ruID):
		self.__reportingUserID = ruID	
	
	reportingUserID = property(getReportingUserID, setReportingUserID)

	
	
	def getQuestionID(self):
		return self.__questionID
	def setQuestionID(self, qID):
		self.__questionID = qID
	questionID = property(getQuestionId, setQuestionID)

