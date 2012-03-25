'''Its a models.py of User app, i.e. it creates a basic model for User app.'''
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
'''
class User(models.Model, object):
	#Here User is a subclass of models.Model and creates an entity named User.
	#	Basically it represents the users of ECODENA.
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
		#postComment method helps a user to comment on any question,
			#Paratmeter: self    --> its an object,
			#			comment --> its a text created by user,
			#						that should be posted as a comment on a specific question.
			#it returns the comment posted by the user.
		comment.userID = self.userID
		comment.timeStamp = datetime.now()
		comment.save()	# save to db

	# input - a query object that already has query text  value set
	def postQuery(self,query):
		#postQuery method helps a user to post a query against the site,
		#	Paratmeter: self  --> its an object,
		#				query --> its a text created by user,
		#						  basically problems that the user is facing regarding site.
		#	it returns the query posted by the user.
		query.userID = self.userID
		query.queryTime = datetime.now()
		query.save()


	def viewProfile(self):
		#viewProfile method helps user to have a view of his/her own profile.
			#And it returns the user profile.
		profile = Profile.objects.filter(userID_f=self.userID)
		return profile

	# input - a profile object that has all fields set except userID
	def saveProfile(self,profile):
		#saveProfile method helps a user to change his/her intials in profile.
		#	And it returns the profile after changing the intials.
		profile.userID_f = self.userID
		profile.save()

class Admin(User, object):
	#Here Admin is a subclass of models.Model and creates an entity named Admin.
	#	Basically it represents the Admins of ECODENA.
	pass
	def resolveQuery(self, queryID, solution):
		query = Query.objects.filter(queryID_f=queryID)
		query.solution = solution
		query.adminID = self.userID
		query.replyTime = datetime.now()
		query.save()

	def deleteComment(self, commentID):
		#deleteComments method helps Admin to delete a comment which is repoted as abuse
		#	or with some another reasons must be deleted.
		#	it returns comment has been deleted.
		comment = Comment.objects.filter(commentID_f=commentID)
		comment.delete()

	def removeUser(self, userID):
		#removeUser method helps Admin to remove User which is creating some problem
		#	or its a fake profile or with some another reasons.
		#	it returns specific User has been removed.
		user = User.objects.filter(userID_f=userID)
		user.delete()

	def removeQuestion(self, questionID):
		#removeQuestion method helps Admin to remove questions from set of questions, by some means.
		#	it returns question  has been deleted.
		question = Question.objects.filter(questionID_f=questionID)
		question.delete()
		
	def removeAttempt(self, attemptID):
		#removeAttempt method helps Admin to remove an attempt from attempts of a specific user, for future reasons.
		#	it returns An Attempt has been removed.
		attempt = Attempt.objects.filter(attemptID_f=attemptID)
		attempt.delete()


	# input - a filled question object
	def addQuestion(self, question):
		#addQuestion helps Admin to add a question to the set of questions.
		#	it returns the set of questions with added questions.
		question.save()
	'''	

class Programmer(User, object):
	'''Here Programmer is a subclass of object and creates an entity named Programmer.
		Basically it represents the users of ECODENA. They can submit their solutions of various problems.
		parameters: User --> its a class that helps a user to log-in to Ecodena.'''
	level_f = models.CharField("Level of User", max_length=20, null=False)

	def getLevel():
		return self.level_f
	def setLevel(level):
		self.level_f = level
	level = property(getLevel,setLevel)


class Profile(models.Model, object):
	'''Here Profile is a subclass of models.Model and creates an entity named Profile.
		Basically it represents the profiles of users and admins of ECODENA.'''
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
		
