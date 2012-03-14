from django.db import models
from Ecodena.Question.models import Question
from Ecodena.User.models import User
from Ecodena.Question.models import TestCase

# Create your models here.


class ErrorReport(models.Model, object):
	errorReportID_f = models.AutoField(primary_key=True)
	timeRequirement_f = models.FloatField("Time Required for compiling")
	memory_f = models.FloatField("Memory Requirement")
	ERROR_TYPE = ((0,'Correct Answer'),(1,'Compilation Error'),(2,'Run Time Error'),(3,'Time limit Exceeded'),(4,'Memory Limit Exceeded'),(5,'Wrong Answer'))
	errorType_f = models.SmallIntegerField(choices=ERROR_TYPE,verbose_name="Types of Errors") 
	errorMessage_f = models.TextField("Error Message generated")
	testCaseLevel_f = models.SmallIntegerField(choices=TestCase.CASE_TYPE, verbose_name="Test Case Level")


	def getTimeRequirement(self):
		return self.timeRequirement_f
	def setTimeRequirement(self,time):
		self.timeRequirement_f = time
	timeRequirement = property(getTimeRequirement,setTimeRequirement)
	

	def getMemory(self):
		return self.memory_f
	def setMemory(self,memory):
		self.memory_f = memory
	memory = property(getMemory,setMemory)


	def getErrorType(self):
		return self.errorType_f
	def setErrorType(self,type):
		self.errorType_f = type
	errorType = property(getErrorType,setErrorType)


	def getErrorMessage(self):
		return self.errorMessage_f
	def setErrorMessage(self,message):
		self.errorMessage_f = message
	errorMessage = property(getErrorMessage,setErrorMessage)


	def getTestCaseLevel (self):
		return self.testCaseLevel_f
	def setTestCaseLevel (self,level):
		self.testCaseLevel_f = level
	testCaseLevel = property(getTestCaseLevel,setTestCaseLevel)


class Attempt(models.Model, object):
	attemptID_f = models.AutoField(primary_key=True)
	questionID_f = models.ForeignKey(Question, verbose_name="Question ID", null=False)
	userID_f = models.ForeignKey(User, verbose_name="User ID", null=False)
	solution_f = models.TextField("Solution uploaded by the User", null=False)
	errorReportID_f = models.ForeignKey(ErrorReport,verbose_name="Error Report for the Solution", null=False)
	status_f = models.BooleanField("Status of attempt - true = right, false = wrong")
	timeOfSubmission_f = models.DateTimeField("Time of Submission", null=False)


	def getAttemptID(self):
		return self.attemptID_f
	def setAttemptID(self,aID):
		self.attemptID_f = aID
	attemptID = property(getAttemptID,setAttemptID)

	
	def isCorrect(self):
		return self.status_f	
	def setStatus(self,status):
		self.status_f = status
	status = property(setStatus) 
		
	
	def getTimeOfSubmission(self):
		return self.timeOfSubmission_f
	def setTimeOfSubmission(self,time):
		self.timeOfSubmission_f = time
	timeOfSubmission = property(getTimeOfSubmission,setTimeOfSubmission)
	
	
	def getUserID(self):
		return self.userID_f
	def setUserID(self,uID):
		self.userID_f = uID
	userID = property(getUserID,setUserID)


	def getErrorReportID(self):
		return self.errorReportID_f
	def setErrorReportID(self,reportID):
		self.errorReportID_f = reportID
	errorReportID = property(getErrorReportID,setErrorReportID)

