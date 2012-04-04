#It controls the views of the Attempts

from django.http import HttpResponse
from Attempt.models import Attempt
#from User.models import User
import Compiler
from Compiler.dictionary import compilers
from Compiler.models import Language
from Compiler.models import CompilerVersion
from django import forms
from django.shortcuts import render_to_response, render
from datetime import datetime
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from Compiler.models import CompilerVersion

class SolutionForm(forms.Form):
	'''creates a form for pasting the solution of a question '''
	text = forms.CharField(widget=forms.Textarea)
	cv = CompilerVersion.objects.all()
	cvname = []
	for c in cv:
		cvname.append(c.versionName)
	version = forms.ChoiceField(widget=forms.Select(),choices=cvname)
		
def listSolutions(request):
	'''lists all the solutionIDs' that a particular user has submitted
	parameter:request-->All the details associated with URL 
	returns the solutions.html page and the list of solution ids'''
	if request.user.is_authenticated():
		solutions = Attempt.objects.filter(userID_f=request.user)
		return render(request, 'solutions.html',{'solutions':solutions})
	else:
		return HttpResponse("You need to log in first, only then can you access the url %s" %request.path)

def viewSolution(request,solutionID):
	'''A soluiton whose Id is passed as the parameter is displayed with the AttemptID, question text, level, question type, solution provided by the user, status of the solution and the error report for the solution
	Parameter:request-->All the information of the form is stored in request
	solutionID-->the ID of attempt to be displayed
	If the user is not authenticated then this returns an Http Response stating that the user is not logged in
	If the user is authenticated and the form filled is valid then it returns the page with the solution and other details'''
	if request.user.is_authenticated():
		s = Attempt.objects.filter(attemptID_f=solutionID)
		solution = s.filter(userID_f=request.user)
		if not solution:
			return render(request, 'solution.html',{'solution':solution})
		else :
			return render(request, 'solution.html',)
	else:
		return HttpResponse("You need to log in first, only then can you access the url %s" %request.path)
		
@csrf_protect
def submitSolution(request,questionID):
	'''Uploading of the solution submitted by the user. The necessary details are added to the database and compiler function is called to generate the error report for the concerning Attempt
	Parameter:request-->All the information associated with the url
	returns the submitsolution.html page making the necessary updation of the database.
	'''
	if request.user.is_authenticated():
		version = CompilerVersion.objects.all()
		dt =datetime.now()
		f=SolutionForm()
		dc = { 'form' :f, 'version' :version}
		context = RequestContext(request, dc)
		if request.method =="POST":
			f=SolutionForm(request.POST)
			if not f.is_valid():
				
				return render(request,'submitsolution.html', context)
			else:
				attempt = Attempt()
				#errorReportID=compileSolution()
				dc = { 'errorReportID':errorReportID,'version':version,'dt':dt}
				context = RequestContext(request, dc)
				attempt.solutionText = f.text
				attempt.compilerVersion = f.version
				attempt.questionID = questionID
				attempt.userID = userID
				attempt.timeOfSubmission = datetime.datetime.now()
				attempt.ErrorReport = 6
				attempt.save()
				return render(request, 'submitsolution.html', context) 
			
			#language = Language.objects.all()
			
		return render(request, 'submitsolution.html',context)
	else:
		return HttpResponse("You need to log in first, only then can you access the url %s" %request.path)
		
def compileSolution(version,solution,question):
	'''compiles the solution by calling the appropriate compiler 
	Parameter:version-->contains the version of the compiler that the user has selected
	Parameter:soluiton-->contains the solution object to be compiled
	Parameter:question-->contains the question object so that the appropriate test cases can be fetched.
	returns nothing if the appropriate compiler is available else it gives an error saying compiler not available'''
	compiler_ver_lang = version.versionName + ' ' + version.language.languageName
	if compiler_ver_lang in compilers:
		compiler = compilers[compiler_ver_lang]
		errorReportID = compiler()
	else: 
		print"Compiler not available"
	
	
	
