# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms
from Question.models import Level
from Question.models import Type
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from Question.models import Question
from ProblemSetter.models import HasSet
from django.shortcuts import render


class ProblemForm(forms.Form):
	problemTitle = forms.CharField()
	problemText = forms.CharField(widget=forms.Textarea)
	#levels=Level.objects.all()
		
	level=forms.CharField()
	#types=Type.objects.all()
	
	type=forms.CharField()
	

def ViewProblemSet(request):
	if request.user.is_authenticated():
		questionID = HasSet.objects.filter(userID_f=request.user)
		
		return render(request,'questionList.html',{'questionID':questionID})
	else:
		return HttpResponse("You need to log in to view list of problems submitted by %s" %request.path)
			
def ViewProblem(request,questionID):
	qID=HasSet.objects.filter(questionID_f=questionID)[0]
	return render(request,'particularQuestion.html',{'questionID':qID})
@csrf_protect
def UploadProblem(request):
	if request.user.is_authenticated():
		f=ProblemForm()
		dc={'form':f}
		context = RequestContext(request,dc)
		if request.method =="POST":
			f=ProblemForm(request.POST)	
			context = RequestContext(request,dc)
			if not f.is_valid():
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
	else:
		return HttpResponse("You need to log in first, only then can you access the url %s" %request.path)
		
def DeleteProblem(request,qID):
	questionID=HasSet.objects.filter(questionID=qID)
	questionID.delete()
	return HttpResponse("Question Deleted Successfully")	
