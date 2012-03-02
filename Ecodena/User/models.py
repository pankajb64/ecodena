from django.db import models

# Create your models here.

class User(models.Model):
	userID = models.AutoField(primary_key=True)
	userName = models.CharField("User name", max_length=30, null=False)
	password = models.CharField("Password", max_length=12, null=False)
	isProgrammer = models.BooleanField("Is a Programmer", default=True)
	isAdmin = models.BooleanField("Is Administrator", default=False)
	userEmail = models.EmailField("Email ID of User", max_length=75)
	numberOfAttempts = models.IntegerField("Number of Attempts")
	
	#def getUserID(self)
	#def getEmailID(self)
	#def getNumberOfAttempts(self)
	#det setNumberOfAttempts(self, numberofAttempts)
	#def postComment(self, questionID, comment)
	#def postQuery(self, query)
	#def viewProfile(self)
	#def saveProfile(self, user)

class Admin(User):
	pass
	#def resolveQuery(self, qID)
	#def deleteComment(self, commentID)
	#def removeUser(self, uID)
	#def removeQuestion(self, questionID)
	#def removeAttempt(self, attemptID)
	#def addProblem(self, problem)

class Programmer(User):
	level = models.CharField("Level of User", max_length=20, null=False)
	#def getLevel(self)
	#def setLevel(self, level)

