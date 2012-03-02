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


	#def getCommentText(self)
	#def setCommentText(self, comment)
	#def getTimeStamp(self)
	#def setTimeStamp(self, Timestamp)
	#def isReported(self)
	#def report(self, status)
	#def getUserID(self)
	#def setUserID(self, uID)
	#def getReportingUserID(self)
	#def setReportingUserID(self, ruID)
	#def getQuestionID(self)
	#def setQuestionID(self, qID)
