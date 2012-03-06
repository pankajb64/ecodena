from django.db import models

# Create your models here.

class User(models.Model):
	userID_f = models.AutoField(primary_key=True)
	userName_f = models.CharField("User name", max_length=30, null=False)
	password_f = models.CharField("Password", max_length=12, null=False)
	isProgrammer_f = models.BooleanField("Is a Programmer", default=True)
	isAdmin_f = models.BooleanField("Is Administrator", default=False)
	userEmail_f = models.EmailField("Email ID of User", max_length=75)
	numberOfAttempts_f = models.IntegerField("Number of Attempts")


	def getUserID(self):
		return self.__getUserID 
	userID = property(getUserID)	


	def getEmailID(self):
		return self.__userEmail
	userEmail = property(getEmailID)
	

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
		q	#database work

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
		#database work

class Admin(User):
	pass
	#def resolveQuery(self, qID)
	#def deleteComment(self, commentID)
	#def removeUser(self, uID)
	#def removeQuestion(self, questionID)
	#def removeAttempt(self, attemptID)
	#def addProblem(self, problem)

class Programmer(User):
	level_f = models.CharField("Level of User", max_length=20, null=False)

	def getLevel():
		return self.__level
	def setLevel(level):
		self.__level = level
	level = property(getLevel,setLevel)

