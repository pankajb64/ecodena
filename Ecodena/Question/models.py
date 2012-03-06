from django.db import models

# Create your models here.



class Level(models.Model):
	levelID_f = models.AutoField(primary_key=True)
	levelName_F = models.CharField("Level Name", max_length = 20 , null = False)
	

class Type(models.Model):
	typeID_f = models.AutoField(primary_key=True)
	typeName_f = models.CharField("Type Name" , max_length = 30 , null = False)


class Question(models.Model):
	questionID_f = models.AutoField(primary_key=True)
	questionText_f = models.TextField("Problem Statement", null=False)
	questionTitle_f = models.CharField("Problem Title", max_length = 50, null = False) 
	level_f = models.ForeignKey(Level, verbose_name="Question Level", null=False)
	type_f = models.ForeignKey(Type, verbose_name="Type of Question", null=False)
	timeLimit_f = models.FloatField("Time Limit for Question",null=False)
	commentList_f = []
	testCasesList_f = []
	
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
	caseID_f = models.AutoField(primary_key=True)
	questionID_f = models.ForeignKey(Question , verbose_name="Question ID", null=False)
	CASE_TYPE = ((0, 'Low'), (1, 'Medium'), (2, 'High'))
	caseType_f = models.SmallIntegerField(choices=CASE_TYPE, verbose_name="Type of Case")
	input_f = models.TextField("Input")	
	output_f = models.TextField("Output")
	

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
