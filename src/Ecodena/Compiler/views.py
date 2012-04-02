# Create your views here.
import models
from models import *
from CCompiler111 import *

def CCompile111(question, attempt, testcase):

	c = CCompiler111()
	c.language = Language.objects.filter(languageName_f='C')[0]
	c.CompilerVersion = CompilerVersion.objects.filter(versionName_f='1.1.1')[0]
	c.question = question
	c.attempt = attempt
	c.testcase = testcase
	c.errorReport = None
	print "running CCompile111"
	return c.compile()
	
def JavaCompile111(question, attempt, testcase):

	java = JavaCompiler111()
	java.language = Language.objects.filter(languageName_f='Java')[0]
	java.CompilerVersion = CompilerVersion.objects.filter(versionName_f='1.1.1')[0]
	java.question = question
	java.attempt = attempt
	java.testcase = testcase
	java.errorReport = None

	return java.compile()
