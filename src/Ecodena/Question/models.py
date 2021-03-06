#This file creates the models of Question
from django.db import models

# Create your models here.



class Level(models.Model):
	'''Creates the entity Level which is a subclass of models.Model class
	'''
	levelID_f = models.AutoField(primary_key=True)
	levelName_f = models.CharField("Level Name", max_length = 20 , null = False, unique=True)

	def getLevelName(self):
		return self.levelName_f
	
	def setLevelName(self, lname):
		self.levelName_f =lname
	
	levelName = property(getLevelName, setLevelName)		
	
	class Meta:
		verbose_name = 'level'
		verbose_name_plural = 'levels'

	def __unicode__(self):
		return self.levelName
	
	

class Type(models.Model):
	'''Creates the entity Type which is a subclass of models.Model class'''
	typeID_f = models.AutoField(primary_key=True)
	typeName_f = models.CharField("Type Name" , max_length = 30 , null = False)

	class Meta:
		verbose_name = 'type'
		verbose_name_plural = 'types'

	def __unicode__(self):
		return self.typeName_f


class Question(models.Model, object):
	'''Creates the entity question 
	which is a subclass of models.Model'''
	questionID_f = models.AutoField(primary_key=True)
	questionText_f = models.TextField("Problem Statement", null=False)
	questionTitle_f = models.CharField("Problem Title", max_length = 50, null = False) 
	level_f = models.ForeignKey(Level, verbose_name="Question Level", null=False)
	type_f = models.ForeignKey(Type, verbose_name="Type of Question", null=False)
	timeLimit_f = models.FloatField("Time Limit for Question",null=False)
	commentList_f = []
	LowtestCasesList_f = []
	MedtestCasesList_f = []
	HightestCasesList_f = []
	
	questionPoints_f = models.FloatField("The points for the question",null = False)
	questionRating_f = models.FloatField("The rating for the question",null = False)
	
	
	def getQuestionID(self):
		return self.questionID_f
	def setQuestionID(self,qID):
		self.questionID_f=qID
	questionID = property(getQuestionID,setQuestionID)
	

	def getQuestionText(self):
		return self.questionText_f
	def setQuestionText(self,qtext):
		self.questionText_f = qtext
	questionText = property(getQuestionText,setQuestionText) 
	

	def getQuestionTitle(self):
		return self.questionTitle_f
	def setQuestionTitle(self,title):
		self.questionTitle_f = title
	questionTitle = property(getQuestionTitle, setQuestionTitle)
	
	def getComments(self):
		return self.commentList_f
	def addComments(self,comment):
		#add comments to the end of comment list
		commentList.append(comment)	
	def setCommentList(self,commentList):
		self.commentList_f = commentList
	commentList = property(getComments,setCommentList)
	

	def getTestCasesList(self):
		return self.testCasesList_f
	def setTestCasesList(self,testCasesList):
		self.testCasesList_f = testCasesList
	def removeTestCase(self,caseID):
		#deletes the Test Case
		del self.testCasesList_f[caseID]
	testCasesList = property(getTestCasesList,setTestCasesList)

	def getLowTestCasesList(self):
		return self.LowtestCasesList_f
	def setLowTestCasesList(self,testCasesList):
		self.LowtestCasesList_f = testCasesList
	
	def getMedTestCasesList(self):
		return self.MedtestCasesList_f
	def setMedTestCasesList(self,testCasesList):
		self.MedtestCasesList_f = testCasesList
	
	def getHighTestCasesList(self):
		return self.HightestCasesList_f
	def setHighTestCasesList(self,testCasesList):
		self.HightestCasesList_f = testCasesList
		
	class Meta:
		verbose_name = 'question'
		verbose_name_plural = 'questions'

	def __unicode__(self):
		return self.questionTitle


class BattleQuestion:
	pass

class TestCase(models.Model, object):
	'''Creates the entity TestCase which is a subclass of models.Model'''
	caseID_f = models.AutoField(primary_key=True)
	questionID_f = models.ForeignKey(Question , verbose_name="Question ID", null=False)
	CASE_TYPE = ((0, 'Low'), (1, 'Medium'), (2, 'High'))
	caseType_f = models.SmallIntegerField(choices=CASE_TYPE, verbose_name="Type of Case")
	input_f = models.TextField("Input")	
	output_f = models.TextField("Output")
	

	def getTestID(self):
		return self.caseID_f
	def setTestID(self,tID):
		self.caseID_f = tID 
	caseID = property(getTestID,setTestID)


	def getCaseType(self):
		return self.caseType_f
	def setCaseType(self,ctype):
		self.caseType_f = ctype
	caseType = property(getCaseType,setCaseType)	
	

	def getOutput(self):
		return self.output_f
	def setOutput(self,text):
		self.output_f = text
	output = property(getOutput,setOutput)
	
	def getQuestion(self):
		return self.questionID_f
	def setQuestion(self,qID):
		self.questionID_f = qID
	questionID = property(getQuestion,setQuestion)

	class Meta:
		verbose_name = 'test case'
		verbose_name_plural = 'test cases'

	def __unicode__(self):
		return `self.caseID` + ' ' + `self.questionID` + ' ' + `self.caseType`
		
