# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from models import Query
from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext
from django.shortcuts import render_to_response

class QueryForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	#class Meta:
	#	model = Query

def postQuery(request,userID):
	f=QueryForm
	dc = { 'form' :f} 
	context = RequestContext(request, dc)
	Timestamp=datetime.now()
	if request.method == 'POST':
		f=QueryForm(request.POST)
		if not f.is_valid():
			return render_to_response('postquery.html',context)
		else:
			q=Query()
			q.queryText=f['text'].data
			q.userID=User.objects.filter(username=userID)[0]
			q.queryTime=Timestamp
			q.save()
			qID=q.queryID
			dc = {'queryID' :qID}
			context = RequestContext(request,dc)
			return render_to_response('postquery.html',context)
	return render_to_response('postquery.html',context)
