# Create your views here.

from django.http import HttpResponse
from Attempt.models import Attempt
#from User.models import User
import Compiler
from Compiler.models import Language
from Compiler.models import CompilerVersion
from django import forms
from django.shortcuts import render_to_response
from datetime import datetime
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

class SolutionForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	version = forms.ChoiceField()
		
def listSolutions(request,userID):
	solutions = Attempt.objects.filter(userID_f=User.objects.filter(username=userID)[0])
	return render_to_response('solutions.html',{'solutions':solutions})

def viewSolution(request,userID,solutionID):
	s = Attempt.objects.filter(attemptID_f=solutionID)
	solution = s.filter(userID_f=User.objects.filter(username=userID)[0])[0]
	return render_to_response('solution.html',{'solution':solution, 's':s})

@csrf_protect
def submitSolution(request):
	version = CompilerVersion.objects.all()
	dt =datetime.now()
	f=SolutionForm()
	dc = { 'form' :f, 'version' :version}
	context = RequestContext(request, dc)
	if request.method =="POST":
		f=SolutionForm(request.POST)
		if not f.is_valid():
			
			return render_to_response('submitsolution.html', context)
		else:
			attempt = Attempt()
			errorReportID=compileSolution()
			dc = { 'errorReportID':errorReportID,'version':version,'dt':dt}
			context = RequestContext(request, dc)
			return render_to_response('submitsolution.html', context) 
		
		#language = Language.objects.all()
		
	return render_to_response('submitsolution.html',context)
	
def compileSolution(version,solution,question):
	compiler_ver_lang = version.versionName + ' ' + version.language.languageName
	if compiler_ver_lang in compilers:
		compiler = compilers[compiler_ver_lang]
		errorReportID = compiler()
	else: 
		print"Compiler not available"
	
	
	
