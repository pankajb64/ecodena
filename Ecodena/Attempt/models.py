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
	
	#def getTimeRequirement(self)
	#def setTimeRequirement(self, time)
	#def getMemory(self)
	#def setMemory(self, memory)
	#def getErrorType(self)
	#def setErrorType(self, type)
	#def getErrorMessage(self)
	#def setErrorMessage(self, message)
	#def getTestCaseLevel (self)
	#def setTestCaseLevel (self, level)

class Attempt(models.Model):
	attemptID = models.AutoField(primary_key=True)
	questionID = models.ForeignKey(Question, verbose_name="Question ID", null=False)
	userID = models.ForeignKey(User, verbose_name="User ID", null=False)
	solution = models.TextField("Solution uploaded by the User", null=False)
	errorReportID = models.ForeignKey(ErrorReport,verbose_name="Error Report for the Solution", null=False)
	status = models.BooleanField("Status of attempt - true = right, false = wrong")
	timeOfSubmission = models.DateTimeField("Time of Submission", null=False)

	# def getAttemptID(self)
	# def setAttemptID(self, aID)
	# def isCorrect(self)
	# def setStatus(self, status)
	# def getTimeOfSubmission(self)
	# def setTimeOfSubmission(self, time)
	# def getUserID(self)
	# def setUserID(self, uID)
	# def getErrorReport(self)
	# def setErrorReport(self, report)

