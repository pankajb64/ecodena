from django.db import models
#from Ecodena.User.models import User
from Ecodena.Question.models import Question
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model, object):
	commentID_f = models.AutoField(primary_key=True)
	commentText_f = models.TextField("The Body of the Comment", null=False)
	isReported_f = models.BooleanField("Is the comment Reported ?", default=False)
	userID_f = models.ForeignKey(User, verbose_name="User ID", null=False, related_name='+' )
	reportingUserID_f =  models.ForeignKey(User, verbose_name="User who reported this comment",  blank=True, null=True)
	questionID_f = models.ForeignKey(Question, verbose_name="Question ID", null=False)
	timeStamp_f = models.DateTimeField("Time of Posting", null=False)


	def getCommentText(self):
		return self.commentText_f
	def setCommentText(self, comment):
		self.commentText_f = comment
	commentText = property(getCommentText, setCommentText)

	
	
	def getTimeStamp(self):
		return self.timeStamp_f
	def setTimeStamp(self, Timestamp):
		self.timeStamp_f = Timeastamp
	timeStamp = property(getTimeStamp, setTimeStamp)

	

	def isReported(self):
		return isReported

		
	def report(self, status):
		self.isReported_f = status
	
	isReported = property(isReported, report)

	def getUserID(self):
		return self.userID_f 
	def setUserID(self, uID):
		self.userID_f = uID
	userID = property(getUserID, setUserID)	
	

	def getReportingUserID(self):
		return self.reportingUserID_f
	def setReportingUserID(self, ruID):
		self.reportingUserID_f = ruID	
	
	reportingUserID = property(getReportingUserID, setReportingUserID)

	
	
	def getQuestionID(self):
		return self.questionID_f
	def setQuestionID(self, qID):
		self.questionID_f = qID
	questionID = property(getQuestionID, setQuestionID)

	class Meta:
		verbose_name = 'comment'
		verbose_name_plural = 'comments'

	def __unicode__(self):
		return `self.commentID_f` + ' ' + `self.userID` + ' ' + `self.questionID`
		
