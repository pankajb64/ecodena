''' Its our Post Query app's views.py, i.e. how Post Query app will shown to user'''
from datetime import datetime
from django.http import HttpResponse
from models import Query
from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext
from django.shortcuts import render_to_response,render

class QueryForm(forms.Form):
	''' Its a form which user have to fill in order to post a query'''
	text = forms.CharField(widget=forms.Textarea)
	#class Meta:
	#	model = Query

def postQuery(request):
	'''Method will provide a form to user, method wil note down the time, date and userID of the user, 
		before all this method will check wether the user is authenticated or not,
		if authenticated the user will be able to post query 
		and if not authenticated then a message will pop-up user has to login first. 
		Parameter: request --> All the information of the form is stored in request. 
		Function will return a Post query html page.'''
	if request.user.is_authenticated():
		
		f=QueryForm
		dc = { 'form' :f} 
		context = RequestContext(request, dc)
		Timestamp=datetime.now()
		if request.method == 'POST':
			f=QueryForm(request.POST)
			if not f.is_valid():
				return render(request,'postquery.html',context)
			else:
				q=Query()
				q.queryText=f['text'].data
				q.userID=User.objects.filter(username=userID)[0]
				q.queryTime=Timestamp
				q.save()
				qID=q.queryID
				dc = {'queryID' :qID}
				context = RequestContext(request,dc)
				return render(request,'postquery.html',context)
		return render(render,'postquery.html',context)

	else:
		return HttpResponse("You need to log in first, only then can you access the url %s" %request.path)
