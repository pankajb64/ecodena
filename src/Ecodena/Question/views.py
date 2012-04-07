#It controls the views of Question 
from django.http import HttpResponse, HttpResponseRedirect
from Question.models import Question
from Comment.models import Comment
from django.shortcuts import render_to_response, render
from datetime import datetime
from django import forms
from django.template import RequestContext
from Ecodena.Attempt.models import *


class CommentForm(forms.Form):
	'''Creates a form for writing a comment'''
	text = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':66}), label="Enter the Text to comment", initial="")
	
	
def test(request):
	return HttpResponse("<h1>It works!</h1>")


def listQuestions(request):
	'''list all the questions with its title
	parameter:request-->All the details associated with URL 
	returns the question.html webpage and the list of questions'''
	questions = Question.objects.all()
	return render(request, 'questions.html',{'questions':questions})

def viewQuestionByID(request, questionID):
	'''A question whose Id is passed as the parameter is displayed with the question title, question text, comment list
	Parameter:request-->All the information of the form is stored in request
	questionID-->the ID of question to be displayed
	If the user is not authenticated then this returns an Http Response stating that the user is not logged in
	If the user is authenticated and the form filled is valid then it returns the page with the question and other details'''
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
					form = CommentForm()
				else:
					return HttpResponseRedirect("/login?next=%s" %questionID)
						
					
		question.commentList_f = list(Comment.objects.filter(questionID_f = question))
		return render(request, 'question.html',RequestContext(request, {'question' : question, 'form' : form}))
	else:
		return render(request, 'question.html', RequestContext(request))	
#	return HttpResponse("%s" %questions)

def generatePoints(request):
	
		questionPoints_f = level_f.levelID_f * 20
		#assuming 5 levels... for n levels i should be 100/n
		
		return questionPoints_f

def generateRating(request):
		numberOfUsers = Attempt.objects.filter(questionID_f = request.questionID_f).distinct('userID_f').filter(status = True).count()
		totalUsers = Attempt.objects.distinct('userID_f').count()
		
		a = 0.25
		p1 = pow((numberOfUsers/totalUsers),a)
		# this shows the ratio of users able to solve the question
	
		totalUsers_f = Attempt.objects.filter(questionID_f = request.questionID_f).distinct('userID_f').count()
		b = 0.25
		p2 = pow((numberOfUsers/totalUsers_f),b)
		#this shows the accuracy of the rating
		
		questionPoints_f = level_f.levelID_f * 20
		#assuming 5 levels... for n levels i should be 100/n
		
		c = 0.125
		p3 = pow((questionPoints_f/100),c)
		#this shows the difficulty of the problem
		
		questionRatings_f = 10 *p1*p2*p3
		return questionRating_f
