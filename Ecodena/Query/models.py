from django.db import models
from Ecodena.User.models import User
import datetime

# Create your models here.

class Query(models.Model, object):
	queryID_f = models.AutoField(primary_key=True)
	queryText_f = models.TextField("The Text explaining the Query", null=False)
	solution_f = models.TextField("The Solution of the Query")
	userID_f = models.ForeignKey(User, verbose_name="User ID of user posting the query", null=False, related_name='+')
	adminID_f = models.ForeignKey(User, verbose_name="User ID of admin resolving the query", related_name='+')
	queryTime_f = models.DateTimeField("Time of posting Query", null=False)
	replyTime_f = models.DateTimeField("Time of resolving Query", )


	def getQueryText(self):
		return self.__queryText
	def setQueryText(self, text):
		self.__queryText = text
	queryText = property(getQueryText, setQueryText)

	
	def getQueryID(self):
		return self.__queryID
	def setQueryID(self, qID):
		self.__queryID = qID
	queryID = property(getQueryID, setQueryID)


	def getSolution(self):
		return self.__solution
	def setSolution(self, code):
		self.__solution = code
	solution = property(getSolution, setSolution)


	def getQueryTime(self):
		return self.__queryTime
	def setQueryTime(self, Timestamp):
		Timestamp = datetime.datetime.now()
		self.__queryTime = Timestamp
	queryTime = property(getQueryTime, setQueryTime)


	def getReplyTime(self):
		return self.__replyTime
	def setReplyTime(self, Timestamp):
		Timestamp = datetime.datetime.now()
		self.__replyTime = Timestamp
	replyTime = property(getReplyTime, setReplyTime)
	

	def getUserID(self):
		return self.__userID
	def setUserID(self, uID):
		self.__userID = uID
	userID = property(getUserID, setUserID)


	def getAdminID(self):
		return self.__adminID
	def setAdminID(self, aID):
		self.__adminID = aID
	adminID = property(getAdminID, setAdminID)


