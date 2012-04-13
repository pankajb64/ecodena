# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from Question.models import *
#from Question.models import Type
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from Question.models import Question
from ProblemSetter.models import HasSet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class ProblemForm(forms.ModelForm):
	'''problemTitle = forms.CharField()
	problemText = forms.CharField(widget=forms.Textarea)
	levels=list(Level.objects.all())
	choices = []
	for count, level in enumerate(levels):
		choices.append((count, level.levelName_f))
		 	
	level=forms.ChoiceField(choices=choices)
	#types=Type.objects.all()
	
	type=forms.ChoiceField()
	timeLimit = forms.FloatField()'''
	class Meta:
		model = Question



class TestCaseForm(forms.Form):
	CASE_TYPE = ((0, 'Low'), (1, 'Medium'), (2, 'High'))
	caseType = forms.ChoiceField(choices=CASE_TYPE,required=False)
	
	input = forms.FileField(required=False)
	output = forms.FileField(required=False)

@login_required(login_url="/login/")	
def ViewProblemSet(request):
	questionID = HasSet.objects.filter(userID_f=request.user)
		
	return render(request,'questionList.html',{'questionID':questionID})
	
@login_required(login_url="/login/")				
def ViewProblem(request,questionID):
	qID=HasSet.objects.filter(questionID_f=questionID)[0]
	return render(request,'particularQuestion.html',{'questionID':qID})
@csrf_protect
@login_required(login_url="/login/")	
def UploadProblem(request):

	f=ProblemForm()
	dc={'form':f}
	context = RequestContext(request,dc)
	if request.method =="POST":
		f=ProblemForm(request.POST)	
		context = RequestContext(request,dc)
		if not f.is_valid():
			dc={'form':f}
			context = RequestContext(request,dc)
			return render(request,'submitProblem.html', context)
		else:				
			hasSet = HasSet()
			question=Question()
			question.questionText = f.cleaned_data['problemText']
			question.questionTitle = f.cleaned_data['problemTitle']
			question.level.level = f.cleaned_data['level']
			question.type.typeName_f = f.cleaned_data['type']
			question.save()
			hasSet.questionID=question
			hasSet.userID=request.user
			hasSet.save()
			dc={'question':question,'hasSet':hasSet}
			context = RequestContext(request, {'form':f,'question':question,'hasSet':hasSet})
			return HttpResponse("Your question has been sent to admin for approval %s"%request.path)
	else:
		return render(request,'submitProblem.html', context)


@csrf_protect	
@login_required(login_url="/login/")	
def EditProblem(request,qID):
	questionID=Question.objects.filter(questionID_f=qID)[0]
	questionID.LowtestCasesList_f = TestCase.objects.filter(questionID_f=qID).filter(caseType_f=0)
	questionID.MedtestCasesList_f = TestCase.objects.filter(questionID_f=qID).filter(caseType_f=1)
	questionID.HightestCasesList_f = TestCase.objects.filter(questionID_f=qID).filter(caseType_f=2)
	
	hasSet = HasSet.objects.filter(questionID_f = qID)[0]
	initialvalues = { 'problemTitle': questionID.questionTitle , 'problemText': questionID.questionText, 'level': questionID.level_f, 'type': questionID.type_f, 'timeLimit':questionID.timeLimit_f }
	
	f=ProblemForm(instance=questionID)
	dc = {'form':f,'questionID':questionID}
	context = RequestContext(request,dc)
	if request.method =="POST":
		f=ProblemForm(request.POST, instance=questionID)	
		context = RequestContext(request,dc)
		if not f.is_valid():
			dc={'form':f, 'questionID':questionID }
			context = RequestContext(request,dc)
			return render(request,'editProblem.html', context)
		else:
			#questionID.delete()
			questionID = f.save() 
			'''if f.cleaned_data['problemTitle']: 
					questionID.questionTitle = f.cleaned_data['problemTitle']	
			if f.cleaned_data['problemText']: 
					questionID.problemText = f.cleaned_data['problemText']		
			if f.cleaned_data['level']:
					questionID.level = f.cleaned_data['level']
			if f.cleaned_data['timeLimit']:
					questionID.timeLimit = f.cleaned_data['timeLimit']
			questionID.save()'''
			hasSet.questionID = questionID
			hasSet.userID = request.user
			hasSet.save()
			dc={'questionID':questionID,'hasSet':hasSet}
			context = RequestContext(request,dc)
			return HttpResponseRedirect('/problemSetter/viewProblems/')
	else:
		
		return render(request,'editProblem.html',context)
	
@csrf_protect	
@login_required(login_url="/login/")	
def AddTestCase(request,questionID):
	
	f = TestCaseForm()
	dc={'form':f}
	context = RequestContext(request,dc)
	if request.method =="POST":
		f=TestCaseForm(request.POST)	
		context = RequestContext(request,dc)
		if not f.is_valid():
			dc={'form':f}
			context = RequestContext(request,dc)
			return render(request,'submitTestCase.html', context)
		else:
			case = TestCase()
			case.caseType = f.cleaned_data['caseType']
			case.save()
			path = "static/storage"
			file_path_in = path + case.caseID_f + '_in' 
			if request.FILES['input']:
				handle_uploaded_file(request.FILES['file'],file_path_in)
			file_path_out = path + case.caseID_f + '_ans'
			if request.FILES['output']:
				handle_uploaded_file(request.FILES['file'],file_path_out)  
			case.input_f = file_path_in
			case.output_f = file_path_out
			case.save()
			return HttpResponseRedirect('problemSetter/viewProblems/')
	else:
		return render(request,'addTestCase.html', context)
	
@csrf_protect	
@login_required(login_url="/login/")	
def EditTestCase(request,qID,caseID):
	case = TestCase.objects.filter(caseID = caseID)
	initialvalues = { 'caseType': case.caseType }
	f = TestCaseForm(initial = initialvalues)
	if request.method =="POST":
		f=TestCaseForm(request.POST)	
		context = RequestContext(request,dc)
		if not f.is_valid():
			dc={'form':f}
			context = RequestContext(request,dc)
			return render(request,'editTestCase.html', context)
		else:
			dc = {'form':f,'caseID':caseID,'questionID':qID}
			context = RequestContext(request,dc)
			case.questionID = qID
			path = "static/storage"
			
			if f.cleaned_data['caseType']: 
					case.caseType = f.cleaned_data['caseType']	
			case.save()
			file_path_in = path + case.caseID_f + '_in' 
			if request.FILES['input']:
				handle_uploaded_file(request.FILES['file'],file_path_in)
			file_path_out = path + case.caseID_f + '_ans'
			if request.FILES['output']:
				handle_uploaded_file(request.FILES['file'],file_path_out)  
			case.input_f = file_path_in
			case.output_f = file_path_out
			case.save()
			
			return HttpResponseRedirect('problemSetter/viewProblems/')
	else:
		return render(request,'editTestCase.html', context)
		
def handle_uploaded_file(f, file_name):
	
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    
	
@login_required(login_url="/login/")	 			
def DeleteProblem(request,qID):
	questionID=HasSet.objects.filter(questionID_f=qID)
	questionID.delete()
	ques = Question.objects.filter(questionID_f=qID)
	ques.delete()
	return HttpResponse("Question Deleted Successfully")	
