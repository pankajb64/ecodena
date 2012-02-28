from django.db import models
from Ecodena.Question import Question
from Ecodena.User import User
from Ecodena.Question import TestCase.CASE_TYPE

# Create your models here.

class Attempt(models.Model)
	attemptID = models.AutoField(primary_key=True)
	questionID = models.ForeignKey(Question, verbose_name="Question ID", null=False)
	userID = models.ForeignKey(User, verbose_name="User ID", null=False)
	solution = models.TextField("Solution uploaded by the User", null=False)
	errorReportID = models.ForeignKey(ErrorReport,verbose_name="Error Report for the Solution", null=False)
	status = models.BooleanField("Status of attempt - true = right, false = wrong")
	timeOfSubmission = models.DateTimeField("Time of Submission", null=False)

	# def getAttemptID()
	# def setAttemptID(aID)
	# def isCorrect()
	# def setStatus(status)
	# def getTimeOfSubmission()
	# def setTimeOfSubmission(time)
	# def getUserID()
	# def setUserID(uID)
	# def getErrorReport()
	# def setErrorReport(report)

class ErrorReport(models.Model)
	errorReportID = models.AutoField(primary_key=True)
	timeRequirement = models.FloatField("Time Required for compiling")
	memory = models.FloatField("Memory Requirement")
	ERROR_TYPE = ((0,'Correct Answer'),(1,'Compilation Error'),(2,'Run Time Error'),(3,'Time limit Exceeded'),(4,'Memory Limit Exceeded'),(5,'Wrong Answer'))
	errorType = models.SmallIntegerField(choices=ERROR_TYPE,verbose_name="Types of Errors") 
	errorMessage = models.TextField("Error Message generated")
	testCaseLevel = models.SmallIntegerField(choices=CASE_TYPE, verbose_name="Test Case Level")
	
	#def getTimeRequirement()
	#def setTimeRequirement(time)
	#def getMemory()
	#def setMemory(memory)
	#def getErrorType()
	#def setErrorType(type)
	#def getErrorMessage()
	#def setErrorMessage(message)
	#def getTestCaseLevel ()
	#def setTestCaseLevel (level)

