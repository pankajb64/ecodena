# Create your views here.
import models
from models import *
from CCompiler432 import *
from CppCompiler432 import *
from JavaCompiler160 import *
from PythonCompiler272 import *

def CCompile432(question, attempt, testcase):

	c = CCompiler432()
	c.language = Language.objects.filter(languageName_f='C')[0]
	c.CompilerVersion = CompilerVersion.objects.filter(versionName_f='gcc-4.3.2')[0]
	c.question = question
	c.attempt = attempt
	c.testcase = testcase
	c.errorReport = None
	#print "running CCompile432"
	return c.compile()
	
def JavaCompile160(question, attempt, testcase):

	java = JavaCompiler160()
	java.language = Language.objects.filter(languageName_f='Java')[0]
	java.CompilerVersion = CompilerVersion.objects.filter(versionName_f='javac-1.6.0')[0]
	java.question = question
	java.attempt = attempt
	java.testcase = testcase
	java.errorReport = None

	return java.compile()

def CppCompile432(question, attempt, testcase):

	cpp = CppCompiler432()
	cpp.language = Language.objects.filter(languageName_f='C++')[0]
	cpp.CompilerVersion = CompilerVersion.objects.filter(versionName_f='gcc-4.3.2')[0]
	cpp.question = question
	cpp.attempt = attempt
	cpp.testcase = testcase
	cpp.errorReport = None
	#print "running CppCompile432"
	return cpp.compile()
	
def PythonCompile272(question, attempt, testcase):

	python = PythonCompiler272()
	python.language = Language.objects.filter(languageName_f='Python')[0]
	python.CompilerVersion = CompilerVersion.objects.filter(versionName_f='python-2.7.2')[0]
	python.question = question
	python.attempt = attempt
	python.testcase = testcase
	python.errorReport = None

	return python.compile()
