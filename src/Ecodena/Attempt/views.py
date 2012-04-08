#It controls the views of the Attempts

from django.http import HttpResponse
from Attempt.models import *
from Question.models import *
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
from django.contrib.auth.decorators import login_required
import time

path = "static/storage/solution/"

class SolutionForm(forms.Form):
	'''creates a form for pasting the solution of a question '''
	text = forms.CharField(widget=forms.Textarea, required=False)
	cv = tuple(CompilerVersion.objects.all())
	CHOICES = (('C 1.1.1', 'C 1.1.1'),
               ('b','Dummy'))
	version = forms.ChoiceField(widget=forms.Select(), choices=CHOICES)
	#title = forms.CharField(max_length=50)
	file  = forms.FileField(required=False)
    
	def cleantext(self):
		#val = super(forms.FileField, self.file).clean()
		
		if not ( self.data['file'] or self.data['text']):
			raise forms.ValidationError('Please enter your code in text box or upload an arrpopriate file.')
		return self.data['text']
		
	def clean(self,*args, **kwargs):
		#self.clean_email()
		#self.clean_text()
		if not ( self.cleaned_data['file'] or self.data['text']):
			raise forms.ValidationError('Please enter your code in text box or upload an arrpopriate file.')
		return super(SolutionForm, self).clean(*args, **kwargs)

@login_required(login_url="/login/")		
def listSolutions(request):
	'''lists all the solutionIDs' that a particular user has submitted
	parameter:request-->All the details associated with URL 
	returns the solutions.html page and the list of solution ids'''
	solutions = Attempt.objects.filter(userID_f=request.user)
	return render(request, 'profile.html',{'solutions':solutions})


@login_required(login_url="/login/")
def viewSolution(request,solutionID):
	'''A soluiton whose Id is passed as the parameter is displayed with the AttemptID, question text, level, question type, solution provided by the user, status of the solution and the error report for the solution
	Parameter:request-->All the information of the form is stored in request
	solutionID-->the ID of attempt to be displayed
	If the user is not authenticated then this returns an Http Response stating that the user is not logged in
	If the user is authenticated and the form filled is valid then it returns the page with the solution and other details'''

	solution = Attempt.objects.filter(attemptID_f=solutionID)
	if solution:
		solution = solution[0]
		return render(request, 'solution.html',{'solution':solution})
	else :
		return render(request, 'solution.html',)

		
@csrf_protect
@login_required(login_url="/login/")
def submitSolution(request,questionID):
	'''Uploading of the solution submitted by the user. The necessary details are added to the database and compiler function is called to generate the error report for the concerning Attempt
	Parameter:request-->All the information associated with the url
	returns the submitsolution.html page making the necessary updation of the database.
	'''

	version = CompilerVersion.objects.all()
	dt =datetime.now()
	f=SolutionForm()
	dc = { 'form' :f, 'version' :version}
	context = RequestContext(request, dc)
	if request.method =="POST":
		f=SolutionForm(request.POST, request.FILES)
		if not f.is_valid():
			dc = { 'form' :f, 'version' :version}
			context = RequestContext(request, dc)
			return render(request,'submitsolution.html', context)
		else:
			attempt = Attempt()
			#errorReportID=compileSolution()
			dc = { 'errorReportID':attempt.errorReportID,'version':version,'dt':dt}
			context = RequestContext(request, dc)
			attempt.solutionText = "Main"
			tokens = (f.cleaned_data['version']).split(" ")
			lan = Language.objects.filter(languageName_f=tokens[0])
			version = CompilerVersion.objects.filter(language_f=lan).filter(versionName_f=tokens[1])[0]
			attempt.compilerVersion = version
			attempt.questionID = Question.objects.get(questionID_f=questionID)
			attempt.userID = request.user
			attempt.timeOfSubmission = datetime.now()
			attempt.ErrorReport = ErrorReport(errorType_f=0)
			attempt.save()
			file_name =  path + `attempt.attemptID_f` + "_Main." + attempt.compilerVersion.language.languageName.lower()	
			if request.FILES:
				handle_uploaded_file(request.FILES['file'],file_name)
			else :
				destination = open(file_name, "w")
				destination.write(f.cleaned_data["text"])
				destination.close()	
			attempt.solutionText = file_name
			errorReport = ErrorReport()
			errorReport.errorType_f = 6
			errorReport.save()
			attempt.errorReportID_f = errorReport
			attempt.save()
			#compile()	
			return render(request, 'submitsuccess.html', context) 
		
		#language = Language.objects.all()
		
	return render(request, 'submitsolution.html',context)

def handle_uploaded_file(f, file_name):
	
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
		
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
