from django.db import models
from Ecodena.Question.models import Question
#from Ecodena.User.models import User
from Ecodena.Question.models import Question, TestCase
from django.contrib.auth.models import User
# Create your models here.


class ErrorReport(models.Model, object):
	errorReportID_f = models.AutoField(primary_key=True)
	timeRequirement_f = models.FloatField("Time Required for compiling")
	memory_f = models.FloatField("Memory Requirement")
	ERROR_TYPE = ((0,'Correct Answer'),(1,'Compilation Error'),(2,'Run Time Error'),(3,'Time limit Exceeded'),(4,'Memory Limit Exceeded'),(5,'Wrong Answer'))
	errorType_f = models.SmallIntegerField(choices=ERROR_TYPE,verbose_name="Types of Errors") 
	errorMessage_f = models.TextField("Error Message generated")
	testCaseLevel_f = models.SmallIntegerField(choices=TestCase.CASE_TYPE, verbose_name="Test Case Level where error occured (Select High if solution is correct)")


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

	class Meta:
		verbose_name = 'error report'
		verbose_name_plural = 'error reports'

	def __unicode__(self):
		return `self.errorReportID_f` + ' ' + `self.errorType` + ' ' + self.errorMessage
		

class Attempt(models.Model, object):
	attemptID_f = models.AutoField(primary_key=True)
	questionID_f = models.ForeignKey(Question, verbose_name="Question", null=False)
	userID_f = models.ForeignKey(User, verbose_name="User ID", null=False)
	solution_f = models.TextField("Solution uploaded by the User", null=False)
	errorReportID_f = models.ForeignKey(ErrorReport,verbose_name="Error Report for the Solution", null=True)
	status_f = models.BooleanField("Status of attempt - true = right, false = wrong", blank=True, default=False)
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
	status = property(isCorrect, setStatus) 
		
	
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

	class Meta:
		verbose_name = 'attempt'
		verbose_name_plural = 'attempts'

	def __unicode__(self):
		return `self.userID` + ' ' + `self.attemptID` + ' ' + `self.questionID_f`
	
	'''def question(self):
		return.questionTitle'''
			
