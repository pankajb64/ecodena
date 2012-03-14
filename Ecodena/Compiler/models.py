from django.db import models

# Create your models here.

class Language(models.Model, object)

	languageID_f = models.AutoField(primary_key=True)
	languageName_f = models.CharField("Language Name", max_length=40, null=False)

	def getLanguageName(self):
		return self.languageName_f

	def setLanguageName(self, languageName)
		self.languageName_f = languageName

	languageName = property(getLanguageName, setLanguageName)

class CompilerVersion(models.Model, object)
	versionID_f = models.AutoField(primary_key=True)
	versionName_f = models.CharField("Version Name (Code or Number)", max_length=40, null=False)
	language_f = models.ForeignKey(Language, verbose_name="Language of Compilation", null=False)

	def getVersionName(self):
		return self.versionName_f

	def setVersionName(self, versionName)
		self.versionName_f = versionName

	versionName = property(getVersionName, setVersionName)

	def getLanguage(self):
		return self.language_f

	def setLanguage(self, language)
		self.language_f = language

	language = property(getLanguage, setLanguage)
	
class Compiler():
	
	language = ""
	compilerVersion = ""
	question = None
	attempt = None
	errorReport = None

	#def getLanguage(self)
	#def setLanguage(self, text)
	#def getCompilerVersion(self)
	#def setCompilerVersion(self,text)
	#def getQuestion(self)
	#def setQuestion(self, question)
	#def getAttempt(self, )
	#def setAttempt(self, attempt)
	#def compile(self)
	#def generateErrorReport(self)
