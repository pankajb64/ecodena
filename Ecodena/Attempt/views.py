# Create your views here.

from django.http import HttpResponse
from Attempt.models import Attempt
from User.models import User
from Compiler.models import Language
from Compiler.models import CompilerVersion
from django import newforms as forms
from django.shortcuts import render_to_response
from datetime import datetime

class SolutionForm(forms.Form):
	text = forms.TextField()
		
def listSolutions(request,userID):
	solutions = list(Attempt.objects.filter(userID_f=userID ))
	return render_to_response('solutions.html',{'solutions':solutions})
def viewSolution(request,userID,solutionID):
	s = Attempt.objects.filter(attemptID_f=solutionID )
	solution = s.filter(userID_f=userID)
	return render_to_response('solution.html',{'solution':solution})

def submitSoution(request):
	version = Compiler.objects.all()
	dt =datetime.now()
	if request.method =="POST":
		f=SolutionForm(request.POST)
		if not f.is_valid():
			return render_to_response('submitsolution.html',{'form':f,'version':version})
		else:
			attempt = Attempt()
			
			errorReportID=compileSolution()
			return render_to_response('submitsolution.html',{'errorReportID':errorReportID,'version':version,'dt':dt}) 
		
		#language = Language.objects.all()
	
	
	return render_to_response('submitsolution.html',{'form':f,'version':version})
	
def compileSolution(version,solution,question)
	pass
	
	
