# Create your views here.
from django.http import HttpResponse
from Question.models import Question
from Comment.models import Comment
from django.shortcuts import render_to_response
from datetime import datetime
from django import forms
from django.template import RequestContext

class CommentForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	
	
def test(request):
	return HttpResponse("<h1>It works!</h1>")


def listQuestions(request):
	questions = Question.objects.all()
	return render_to_response('questions.html',{'questions':questions})

def viewQuestionByID(request, questionID):
	question = Question.objects.filter(questionID_f = questionID)
	if question:
		question = question[0]
		form = CommentForm()
#		if request.user.is_authenticated():
		if request.method == "POST":
			form = CommentForm(request.POST)
			
			if form.is_valid():
				if request.user.is_authenticated():
					c = Comment()
					c.commentText = form['text'].data
					c.timeStamp = datetime.now()
					c.isReported = False
					c.userID = request.user
					c.questionID = question
					c.save()
				else:
					return HttpResponse("You need to login first inorder to comment, You noob :) ")
						
					
		question.commentList_f = list(Comment.objects.filter(questionID_f = question))
		return render_to_response('question.html',RequestContext(request, {'question' : question, 'form' : form}))
	else:
		return render_to_response('question.html', RequestContext(request))	
#	return HttpResponse("%s" %questions)

