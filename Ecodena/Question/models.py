from django.db import models

# Create your models here.



class Level(models.Model):
	levelID = models.AutoField(primary_key=True)
	levelName = models.CharField("Level Name", max_length = 20 , null = False)
	

class Type(models.Model):
	typeID = models.AutoField(primary_key=True)
	typeName = models.CharField("Type Name" , max_length = 30 , null = False)


class Question(models.Model):
	questionID = models.AutoField(primary_key=True)
	questionText = models.TextField("Problem Statement", null=False)
	questionTitle = models.CharField("Problem Title", max_length = 50, null = False) 
	level = models.ForeignKey(Level, verbose_name="Question Level", null=False)
	type = models.ForeignKey(Type, verbose_name="Type of Question", null=False)
	timeLimit = models.FloatField("Time Limit for Question",null=False)
	commentList = []
	testCasesList = []
	
	def getQuestionID(self):
		return self.__questionID
	def setQuestionID(self,qID):
		self.__questionID=qID
	questionID = property(getQuestionID,setQuestionID)
	

	def getQuestionText(self):
		return self.__questionText
	def setQuestionText(self,qtext):
		self.__questionText = qtext
	questionText = property(getQuestionText,setQuestionText) 
	

	def getQuestionTitle(self):
		return self.__questionTitle
	def setQuestionTitle(self,title):
		self.__questionTitle = title
	questionTitle = property(getQuestionTitle, setQuestionTitle)
	def getComments(self):
		return self.__commentList
	def addComments(self,comment):
		commentList.append(comment)	
	def setCommentList(self,commentList):
		self.__commentList = commentList
	commentList = property(getComments,setCommentList)
	

	def getTestCasesList(self):
		return self.__testCasesList
	def setTestCasesList(self,testCasesList):
		self.__testCasesList = testCasesList
	def removeTestCase(self,caseID):
		del self.__testCasesList[caseID]
	testCasesList = property(getTestCasesList,setTestCasesList)


class BattleQuestion:
	pass

class TestCase(models.Model):
	caseID = models.AutoField(primary_key=True)
	questionID = models.ForeignKey(Question , verbose_name="Question ID", null=False)
	CASE_TYPE = ((0, 'Low'), (1, 'Medium'), (2, 'High'))
	caseType = models.SmallIntegerField(choices=CASE_TYPE, verbose_name="Type of Case")
	input = models.TextField("Input")	
	output = models.TextField("Output")
	

	def getTestID(self):
		return self.__caseID
	def setTestID(self,tID):
		self.__caseID = tID 
	caseID = property(getTestID,setTestID)


	def getCaseType(self):
		return self.__caseType
	def setCaseType(self,ctype):
		self.__caseType = ctype
	caseType = property(getCaseType,setCaseType)	
	

	def getOutput(self):
		return self.__output
	def setOutput(self,text):
		self.__output = text
	output = property(getOutput,setOutput)
	
	def getQuestion(self):
		return self.__questionID
	def setQuestion(self,qID):
		self.__questionID = qID
	questionID = property(getQuestion,setQuestion)
