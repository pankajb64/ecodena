from django.db import models
from Ecodena.User.models import User

# Create your models here.

class Query(models.Model):
	queryID = models.AutoField(primary_key=True)
	queryText = models.TextField("The Text explaining the Query", null=False)
	solution = models.TextField("The Solution of the Query")
	userID = models.ForeignKey(User, verbose_name="User ID of user posting the query", null=False, related_name='+')
	adminID = models.ForeignKey(User, verbose_name="User ID of admin resolving the query", related_name='+')
	queryTime = models.DateTimeField("Time of posting Query", null=False)
	replyTime = models.DateTimeField("Time of resolving Query", null=False)

	# def getQueryText(self)
	# def setQueryText(self, text)
	# def getQueryID(self)
	# def setQueryID(self, qID)
	# def getSolution(self)
	# def setSolution(self, code)
	# def getQueryTime(self)
	# def setQueryTime(self, Timestamp)
	# def getReplyTime(self)
	# def setReplyTime(self, Timestamp)
	# def getUserID(self)
	# def setUserID(self, uID)
	# def getAdminID(self)
	# def setAdminID(self, aID)

