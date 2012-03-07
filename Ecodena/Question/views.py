# Create your views here.
from django.http import HttpResponse
from Question.models import Question
from Comment.models import Comment
from django.shortcuts import render_to_response
def test(request):
	return HttpResponse("<h1>It works!</h1>")

#def listQuestions():

def viewQuestion(request, questionID):
	question = Question.objects.filter(questionID_f = questionID)
	question.commentList_f = list(Comment.objects.filter(questionID_f = questionID))
	return render_to_response('question.html',{'question' : question})
