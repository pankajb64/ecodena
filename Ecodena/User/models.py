from django.db import models

# Create your models here.

class User(models.Model)
	userID = models.AutoField(primary_key=True)
	userName = models.CharField("User name", max_length=30, null=False)
	password = models.CharField("Password", max_length=12, null=False)
	isProgrammer = models.BooleanField("Is a Programmer", default=True)
	isAdmin = models.BooleanField("Is Administrator", default=False)
	userEmail = models.EmailField("Email ID of User", max_length=75)
	numberOfAttempts = models.IntegerField("Number of Attempts")
	
	#def getUserID()
	#def getEmailID()
	#def getNumberOfAttempts()
	#det setNumberOfAttempts(numberofAttempts)
	#def postComment(questionID, comment)
	#def postQuery(query)
	#def viewProfile()
	#def saveProfile(user)

class Admin(User)
	#def resolveQuery(qID)
	#def deleteComment(commentID)
	#def removeUser(uID)
	#def removeQuestion(questionID)
	#def removeAttempt(attemptID)
	#def addProblem(problem)

class Programmer(User)
	level = models.CharField("Level of User", max_length=20, null=False)
	#def getLevel()
	#def setLevel(level)

