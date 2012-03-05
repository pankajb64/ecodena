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


	def getUserID(self):
		return self.__getUserID 
	userID = property(getUserID)	


	def getEmailID(self):
		return self.__userEmailID
	userEmailID = property(getEmailID)
	

	def getNumberOfAttempts(self):
		return self.__numberOfAttempts
	def setNumberOfAttempts(numberofAttempts):
		self.__numberOfAttempts = numberofAttempts
	numberOfAttempts = property(getNumberOfAttempts,setNumberOfAttempts)
	

	def postComment(self,questionID, comment):
		comment.setQuestionID(questionID)

	def postQuery(self,query):
		q = Query()		
		q.setUserID(self.userID)
		q.setText(query)
		Timestamp = datetime.datetime.now()
		query.setQueryTime(Timestamp)
		q	

	def viewProfile(self):
		x = User()
		x.userName = userName
		x.userEmail = userEmailID
		x.numberOfAttempts = numberOfAttemps
		return x

	def saveProfile(self,user):
		userID = user.getUserID
		userName = user.getUserName
		isProgrammer = user.isProgrammer
		userEmailID = user.userEmailID
		numberOfAttempts = user.numberOfAttempts

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

	def getLevel():
		return self.__level
	def setLevel(level):
		self.__level = level
	level = property(getLevel,setLevel)

