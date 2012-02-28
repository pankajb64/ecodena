from django.db import models
from Ecodena.User import User

# Create your models here.

class Query(models.Model)
	queryID = models.AutoField(primary_key=True)
	queryText = models.TextField("The Text explaining the Query", null=False)
	solution = models.TextField("The Solution of the Query")
	userID = models.ForeignKey(User, verbose_name="User ID of user posting the query", null=False)
	adminID = models.ForeignKey(User, verbose_name="User ID of admin resolving the query")
	queryTime = models.DateTimeField("Time of posting Query", null=False)
	replyTime = models.DateTimeField("Time of resolving Query", null=False)

	# def getQueryText()
	# def setQueryText(text)
	# def getQueryID()
	# def setQueryID(qID)
	# def getSolution()
	# def setSolution(code)
	# def getQueryTime()
	# def setQueryTime(Timestamp)
	# def getReplyTime()
	# def setReplyTime(Timestamp)
	# def getUserID()
	# def setUserID(uID)
	# def getAdminID()
	# def setAdminID(aID)

