# Create your views here.
from django.http import HttpResponse

def test(request):
	return HttpResponse("<h1>It works!</h1>")

#def listQuestions():

#def viewQuestion(request, questionID):

