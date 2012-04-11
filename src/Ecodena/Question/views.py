#It controls the views of Question 
from django.http import HttpResponse, HttpResponseRedirect
from Question.models import Question
from Comment.models import Comment
from Attempt.models import Attempt
from django.shortcuts import render_to_response, render
from datetime import datetime
from django import forms
from django.template import RequestContext
from Ecodena.Attempt.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Ecodena.ProblemSetter.models import *
class CommentForm(forms.Form):
	'''Creates a form for writing a comment'''
	text = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':66}), label="Enter the Text to comment", initial="")
	
	
def test(request):
	return HttpResponse("<h1>It works!</h1>")

class countSuccess(object):
	questionID = None
	success = 0
	accuracy = 0.0
	
	
def listQuestions(request):
	'''list all the questions with its title
	parameter:request-->All the details associated with URL 
	returns the question.html webpage and the list of questions'''
	questions = []
	que = Question.objects.all()
	
	for q in que:
		l = countSuccess()
		l.questionID = q
		l.success = Attempt.objects.filter(questionID_f = q).filter(status_f = True).count()
		c = Attempt.objects.filter(questionID_f=q).count()
		if not c == 0:
			l.accuracy = round((l.success * 1.0/c)*100 , 2)
		else:
			l.accuracy = 0	
		generateRating(q)
		questions.append(l)
	return render(request, 'questions.html',locals())

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

		if request.user.is_authenticated():
				
			var = HasSet.objects.filter(userID_f = request.user).filter(questionID_f = question)
			if var:
				ismyProblem = True
			else:
				ismyProblem = False
		else:
				ismyProblem = False		
		return render(request, 'question.html',RequestContext(request, {'question' : question,'form' : form, 'comments' : question.commentList_f, 'ismyProblem' : ismyProblem} ))
#	return HttpResponse("%s" %questions)

def generatePoints(question):
	
		questionPoints_f = question.level_f.levelID_f * 20
		#assuming 5 levels... for n levels i should be 100/n
		
		return questionPoints_f

def generateRating(question):

	
	#question = Question.objects.get(questionID_f=questionID)
	numberOfUsers = Attempt.objects.filter(questionID_f=question).distinct('userID_f').filter(status_f = True).count()
	totalUsers = Attempt.objects.distinct('userID_f').count()
	
	a = 0.25
	p1 = pow((numberOfUsers*1.0/totalUsers),a)
	# this shows the ratio of users able to solve the question

	totalUsers_f = Attempt.objects.filter(questionID_f=question).count()
	b = 0.25
	p2 = pow((numberOfUsers*1.0/totalUsers_f),b)
	#this shows the accuracy of the rating
	
	question.questionPoints_f = generatePoints(question)
	
	c = 0.125
	p3 = pow((question.questionPoints_f/100.0),c)
	#this shows the difficulty of the problem
	
	question.questionRating_f = round(10 *p1*p2*p3, 1)
	question.save()
	


