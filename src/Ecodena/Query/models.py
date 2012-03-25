'''Its a models.py of post Query, i.e. it creates a basic model for the post Query.'''
from django.db import models
#from Ecodena.User.models import User
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Query(models.Model, object):
	'''Here Query is subclass of models.Model and Creates an entity named Query.'''
	queryID_f = models.AutoField(primary_key=True)
	queryText_f = models.TextField("The Text explaining the Query", null=False)
	solution_f = models.TextField("The Solution of the Query", blank=True)
	userID_f = models.ForeignKey(User, verbose_name="User ID of user posting the query", null=False, related_name='+')
	adminID_f = models.ForeignKey(User, verbose_name="User ID of admin resolving the query", related_name='+', blank=True, null=True)
	queryTime_f = models.DateTimeField("Time of posting Query", null=False)
	replyTime_f = models.DateTimeField("Time of resolving Query", blank=True, null=True)


	def getQueryText(self):
		return self.queryText_f
	def setQueryText(self, text):
		self.queryText_f = text
	queryText = property(getQueryText, setQueryText)

	
	def getQueryID(self):
		return self.queryID_f
	def setQueryID(self, qID):
		self.queryID_f = qID
	queryID = property(getQueryID, setQueryID)


	def getSolution(self):
		return self.solution_f
	def setSolution(self, code):
		self.solution_f = code
	solution = property(getSolution, setSolution)


	def getQueryTime(self):
		return self.queryTime_f
	def setQueryTime(self, Timestamp):
		Timestamp = datetime.datetime.now()
		self.queryTime_f = Timestamp
		

	queryTime = property(getQueryTime, setQueryTime)



	def getReplyTime(self):
		return self.replyTime_f
	def setReplyTime(self, Timestamp):
		Timestamp = datetime.datetime.now()
		self.replyTime_f = Timestamp
	replyTime = property(getReplyTime, setReplyTime)
	

	def getUserID(self):
		return self.userID_f
	def setUserID(self, uID):
		self.userID_f = uID
	userID = property(getUserID, setUserID)


	def getAdminID(self):
		return self.adminID_f
	def setAdminID(self, aID):
		self.adminID_f = aID
	adminID = property(getAdminID, setAdminID)


	class Meta:
		verbose_name = 'query'
		verbose_name_plural = 'queries'

	def __unicode__(self):
		return `self.userID` + ' ' + `self.queryID` + ' ' + self.queryText
		
