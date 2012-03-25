from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
'''
class User(models.Model, object):
	userID_f = models.AutoField(primary_key=True)
	userName_f = models.CharField("User name", max_length=30, null=False)
	password_f = models.CharField("Password", max_length=12, null=False)
	isProgrammer_f = models.BooleanField("Is a Programmer", default=True)
	isAdmin_f = models.BooleanField("Is Administrator", default=False)
	userEmail_f = models.EmailField("Email ID of User", max_length=75)
	numberOfAttempts_f = models.IntegerField("Number of Attempts")


	def getUserID(self):
		return self.getUserID_f 
	userID = property(getUserID)	

	def getEmailID(self):
		return self.userEmail_f
	userEmail = property(getEmailID)
	

	def getNumberOfAttempts(self):
		return self.numberOfAttempts_f
	def setNumberOfAttempts(numberofAttempts):
		self.numberOfAttempts_f = numberofAttempts
	numberOfAttempts = property(getNumberOfAttempts,setNumberOfAttempts)
	
	# input - a comment object that already has comment text and question ID values set
	def postComment(self,comment):
		comment.userID = self.userID
		comment.timeStamp = datetime.now()
		comment.save()	# save to db

	# input - a query object that already has query text  value set
	def postQuery(self,query):
		query.userID = self.userID
		query.queryTime = datetime.now()
		query.save()


	def viewProfile(self):
		profile = Profile.objects.filter(userID_f=self.userID)
		return profile

	# input - a profile object that has all fields set except userID
	def saveProfile(self,profile):
		profile.userID_f = self.userID
		profile.save()

'''

class Admin(User, object):
	pass
	def resolveQuery(self, queryID, solution):
		query = Query.objects.filter(queryID_f=queryID)
		query.solution = solution
		query.adminID = self.userID
		query.replyTime = datetime.now()
		query.save()
'''
	def deleteComment(self, commentID):
		comment = Comment.objects.filter(commentID_f=commentID)
		comment.delete()

	def removeUser(self, userID):
		user = User.objects.filter(userID_f=userID)
		user.delete()

	def removeQuestion(self, questionID):
		question = Question.objects.filter(questionID_f=questionID)
		question.delete()
		
	def removeAttempt(self, attemptID):
		attempt = Attempt.objects.filter(attemptID_f=attemptID)
		attempt.delete()


	# input - a filled question object
	def addQuestion(self, question):
		question.save()
	'''	

class Programmer(User, object):
	level_f = models.CharField("Level of User", max_length=20, null=False)

	def getLevel():
		return self.level_f
	def setLevel(level):
		self.level_f = level
	level = property(getLevel,setLevel)


class Profile (models.Model, object):
	profileID_f = models.AutoField(primary_key=True)
	#name_f = models.CharField("User Display Name", max_length=40)
	dob_f = models.DateField("User Birth Date")
	address_f = models.TextField("User Address")
	GENDER_TYPE = ( (0, 'Male'), (1, 'Female'))
	gender_f = models.SmallIntegerField(choices=GENDER_TYPE, verbose_name="Gender")
	userID_f = models.ForeignKey(User, verbose_name="User ID of user whose profile is this", null=False, unique=True)
	isProgrammer_f = models.BooleanField("Is a Programmer", default=True)
	isAdmin_f = models.BooleanField("Is Administrator", default=False)
	numberOfAttempts_f = models.IntegerField("Number of Attempts")
	
	def getDOB():
		return self.dob_f
	def setDOB(date):
		self.dob_f = date
		
	dob = property(getDOB,setDOB)
		
	def getAddress():
		return address_f
	def setAddress(address):
		self.address_f = address
		
	address = property(getAddress,setAddress)
	
	def getGender():
		return gender_f
	def setGender():
		self.gender_f = gender
		
	gender = property(getGender, setGender)

	def getUserID():
		return userID
		
	def isProgrammer():
		return self.isProgrammer_f
		
	def isAdmin():
		return self.isAdmin_f
		
	def getNumberOfAttempts(self):
		return self.numberOfAttempts_f
	def setNumberOfAttempts(self,attempt):
		self.numberOfAttempts_f = attempt
		
	numberOfAttempts = property(getNumberOfAttempts,setNumberOfAttempts)
