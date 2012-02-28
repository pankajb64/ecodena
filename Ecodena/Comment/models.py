from django.db import models
from Ecodena.User import User
from Ecodena.Question import Question
import datetime

# Create your models here.

class Comment(models.Model)
	commentID = models.AutoField(primary_key=True)
	commentText = models.TextField("The Body of the Comment", null=False)
	isReported = models.BooleanField("Is the comment Reported ?", default=False)
	userID = models.ForeignKey(User, verbose_name="User ID", null=False)
	reportingUserID = = models.ForeignKey(User, verbose_name="User ID of the user who reported this comment")
	questionID = models.ForeignKey(Question, verbose_name="Question ID", null=False)
	timeStamp = models.DateTimeField("Time of Posting", null=False)


	#def getCommentText()
	#def setCommentText(comment)
	#def getTimeStamp()
	#def setTimeStamp(Timestamp)
	#def isReported()
	#def report(status)
	#def getUserID()
	#def setUserID(uID)
	#def getReportingUserID()
	#def setReportingUserID(ruID)
	#def getQuestionID()
	#def setQuestionID(qID)
