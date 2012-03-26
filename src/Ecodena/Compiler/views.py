# Create your views here.
import models
from models import *


def CCompile111(question, attempt):

	c = CCompiler111()
	c.language = Language.objects.filter(languageName_f='C')[0]
	c.CompilerVersion = CompilerVersion.objects.filter(versionName_f='1.1.1')[0]
	c.question = question
	c.attempt = attempt
	c.errorReport = None

	c.compile()
	
def JavaCompile111(question, attempt):

	java = JavaCompiler111()
	java.language = Language.objects.filter(languageName_f='Java')[0]
	java.CompilerVersion = CompilerVersion.objects.filter(versionName_f='1.1.1')[0]
	java.question = question
	java.attempt = attempt
	java.errorReport = None

	java.compile()
