from django.db import models
from Ecodena.Question.models import Question
from Ecodena.User.models import User
from Ecodena.Question.models import TestCase

# Create your models here.


class ErrorReport(models.Model):
	errorReportID = models.AutoField(primary_key=True)
	timeRequirement = models.FloatField("Time Required for compiling")
	memory = models.FloatField("Memory Requirement")
	ERROR_TYPE = ((0,'Correct Answer'),(1,'Compilation Error'),(2,'Run Time Error'),(3,'Time limit Exceeded'),(4,'Memory Limit Exceeded'),(5,'Wrong Answer'))
	errorType = models.SmallIntegerField(choices=ERROR_TYPE,verbose_name="Types of Errors") 
	errorMessage = models.TextField("Error Message generated")
	testCaseLevel = models.SmallIntegerField(choices=TestCase.CASE_TYPE, verbose_name="Test Case Level")


	def getTimeRequirement(self):
		return self.__timeRequirement
	def setTimeRequirement(self,time):
		self.__timeRequirement = time
	timeRequirement = property(getTimeRequirement,setTimeRequirement)
	

	def getMemory(self):
		return self.__memory
	def setMemory(self,memory):
		self.__memory = memory
	memory = property(getMemory,setMemory)


	def getErrorType(self):
		return self.__errorType
	def setErrorType(self,type):
		self.__errorType = type
	errorType = property(getErrorType,setErrorType)


	def getErrorMessage(self):
		return self.__errorMessage
	def setErrorMessage(self,message):
		self.__errorMessage = message
	errorMessage = property(getErrorMessage,setErrorMessage)


	def getTestCaseLevel (self):
		return self.__testCaseLevel
	def setTestCaseLevel (self,level):
		self.__testCaseLevel = level
	testCaseLevel = property(getTestCaseLevel,setTestCaseLevel)


class Attempt(models.Model):
	attemptID = models.AutoField(primary_key=True)
	questionID = models.ForeignKey(Question, verbose_name="Question ID", null=False)
	userID = models.ForeignKey(User, verbose_name="User ID", null=False)
	solution = models.TextField("Solution uploaded by the User", null=False)
	errorReportID = models.ForeignKey(ErrorReport,verbose_name="Error Report for the Solution", null=False)
	status = models.BooleanField("Status of attempt - true = right, false = wrong")
	timeOfSubmission = models.DateTimeField("Time of Submission", null=False)


	def getAttemptID(self):
		return self.__attemptID
	def setAttemptID(self,aID):
		self.__attemptID = aID
	attemptID = property(getAttemptID,setAttemptID)

	
	def isCorrect(self):
		return self.__status	
	def setStatus(self,status):
		self.__status = status
	status = property(setStatus) 
		
	
	def getTimeOfSubmission(self):
		return self.__timeOfSubmission
	def setTimeOfSubmission(self,time):
		self.__timeOfSubmission = time
	timeOfSubmission = property(getTimeOfSubmission,setTimeOfSubmission)
	
	
	def getUserID(self):
		return self.__userID
	def setUserID(self,uID):
		self.__userID = uID
	userID = property(getUserID,setUserID)


	def getErrorReportID(self):
		return self.__errorReportID
	def setErrorReport(self,reportID):
		self.__errorReportID = reportID
	errorReportID = property(getErrorReportID,setErrorReportID)

