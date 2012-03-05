import datetime
from django.db import models
from Ecodena.User import User

Timestamp = datetime.datetime.now()

# Create your models here.

class Query(models.Model)
	queryID = models.AutoField(primary_key=True)
	queryText = models.TextField("The Text explaining the Query", null=False)
	solution = models.TextField("The Solution of the Query")
	userID = models.ForeignKey(User, verbose_name="User ID of user posting the query", null=False)
	adminID = models.ForeignKey(User, verbose_name="User ID of admin resolving the query")
	queryTime = models.DateTimeField("Time of posting Query", null=False)
	replyTime = models.DateTimeField("Time of resolving Query", null=False)

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
		self.__queryTime = Timestamp

	queryTime = property(getQueryTime, setQueryTime)

	def getReplyTime(self):
		return self.__replyTime

	def setReplyTime(self, Timestamp):
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

