from django.db import models

# Create your models here.

class Language(models.Model, object):

	languageID_f = models.AutoField(primary_key=True)
	languageName_f = models.CharField("Language Name", max_length=40, null=False)

	def getLanguageName(self):
		return self.languageName_f

	def setLanguageName(self, languageName):
		self.languageName_f = languageName

	languageName = property(getLanguageName, setLanguageName)


		

class CompilerVersion(models.Model, object):
	versionID_f = models.AutoField(primary_key=True)
	versionName_f = models.CharField("Version Name (Code or Number)", max_length=40, null=False)
	language_f = models.ForeignKey(Language, verbose_name="Language of Compilation", null=False)

	def getVersionName(self):
		return self.versionName_f

	def setVersionName(self, versionName):
		self.versionName_f = versionName

	versionName = property(getVersionName, setVersionName)

	def getLanguage(self):
		return self.language_f

	def setLanguage(self, language):
		self.language_f = language

	language = property(getLanguage, setLanguage)
	
	def languageName(self):
		return self.language_f.languageName

class Compiler():
	
	language = ""
	compilerVersion = ""
	question = None
	attempt = None
	errorReport = None

	
	def getLanguage(self):
		return self._language
	def setLanguage(self, text):
		self._language = text
	language = property(getLanguage,setLanguage)

	def getCompilerVersion(self):
		return self._CompilerVersion
	def setCompilerVersion(self,text):
		self._CompilerVersion = text
	CompilerVersion = property(getCompilerVersion,setCompilerVersion)

	def getQuestion(self):
		return self._question
	def setQuestion(self, question):
		self._question = question
	question = property(getQuestion,setQuestion)

	def getAttempt(self):
		return self._attempt
	def setAttempt(self, attempt):
		self._attempt = attempt
	attempt = property(getAttempt,setAttempt)
		
	#def compile(self)
	#def generateErrorReport(self)
