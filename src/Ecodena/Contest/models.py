from django.db import models
from django.contrib.auth.models import User
from Question.models import Question
import time
import datetime

class ContestHolder(User):
	pass


class Contest(models.Model,object):
	contestID_f=models.AutoField(primary_key=True)
	contestName_f=models.CharField("Name of Contest",max_length=40,null=False)
	contestPwd_f=models.CharField("Password for Contest",max_length=20,null=False)
	termsCond_f=models.TextField("Terms and Conditions")
	adminID_f=models.ForeignKey(User,verbose_name="Admin ID of the admin who approved the contest",null=True,unique=False)
	contestFromDate_f = models.DateField("Date at which contest starts")
	contestToDate_f = models.DateField("Date at which contest ends")
	contestFromTime_f = models.TimeField("Time at which contest starts")
	contestToTime_f = models.TimeField("Time at which contest ends")
	#isApproved = models.BooleanField(("Approval for a contest" , default=False, )
	
	def getContestID(self):
		return self.contestID_f
	def setContestID(self,contestID):
		self.contestID_f=contestID
	
	contestID = property(getContestID,setContestID)
	
	def getContestName(self):
		return self.contestName_f
	def setContestName(self,contestName):
		self.contestName_f = contestName
	
	contestName = property(getContestName,setContestName)		
	
	def getContestPwd(self):
		return self.contestPwd_f
	def setContestPwd(self,contestPwd):
		self.contestPwd_f=contestPwd
	contestPwd = property(getContestPwd,setContestPwd)
	def getTerms(self):
		return self.termsCond_f
	def setTerms(self,terms):
		self.termsCond_f = terms	
	
	termsCond = property(getTerms,setTerms)
			
	def getAdminID(self):
		return self.adminID_f
	def setAdminID(self,adminID):
		self.adminID_f = adminID

	adminID = property(getAdminID,setAdminID)
	
	def getStartTime(self):
		return self.contestFromTime_f
	def setStartTime(self,contestFromTime):
		self.contestFromTime_f = contestFromTime
	contestFromTime = property(getStartTime,setStartTime)
	
	def getStartDate(self):
		return self.contestFromDate_f
	def setStartDate(self,contestFromDate):
		self.contestFromDate_f = contestFromDate
	contestFromDate = property(getStartDate,setStartDate)
	
	def getFinishTime(self):
		return self.contestToTime_f
	def setFinishTime(self,contestToTime):
		self.contestToTime_f = contestToTime
	contestToTime = property(getFinishTime,setFinishTime)
	
	def getFinishDate(self):
		return self.contestToDate_f
	def setFinishDate(self,contestToDate):
		self.contestToDate_f = contestToDate
	contestToDate = property(getFinishDate,setFinishDate)

	def isOver(self):
		#c = contestToTime_f 
		c1 = datetime.datetime.now().time()
		if c > c1:
			return False
		else:
			return True
					
	class Meta:
		verbose_name = 'contest'
		verbose_name_plural = 'contests'
	def __unicode__(self):
		return self.contestName					
	
class ContestQuestion(Question):
	contestID_f=models.ForeignKey(Contest,verbose_name="ContestID of the contest",null=False)
	
	def getContestID(self):
		return self.contestID_f
	def setContestID(self,contestID):
		self.contestID_f=contestID
	
	contestID = property(getContestID,setContestID)
	
	

	
	class Meta:
		verbose_name = 'Contest question'
		verbose_name_plural = 'Contest questions'
	def __unicode__(self):
		return `self.questionID`+' '+`self.contestID`
		
							
class ContestParticipants(models.Model,object):
	contestID_f=models.ForeignKey(Contest,verbose_name="ContestID of the contest",null=False)
	userID_f=models.ForeignKey(User,verbose_name="UserID of the participants",null=False)
	score = models.IntegerField("Score of the Participant")	
	def getContestID(self):
		return self.contestID_f
	def setContestID(self,contestID):
		self.contestID_f=contestID	
	
	contestID = property(getContestID,setContestID)
	
	def getUserID(self):
		return self.userID_f
	def setUserID(self,userID):
		self.userID_f=userID_f
	
	userID = property(getUserID,setUserID)	
	class Meta:
		verbose_name = 'Contest Participant'
		verbose_name_plural = 'Contest Participants'
	def __unicode__(self):
		return `self.contestID`+' '+`self.userID`		

# Create your models here.
