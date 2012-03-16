# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from Query.models import Query
from User.models import User
from django import newforms as forms
from django.shortcuts import render_to _response

class QueryForm(forms.Form):
	text = forms.Textfield()

def postQuery(request,userID):
	f=QueryForm
	Timestamp=datetime.now()
	if request.method == 'POST':
		f=QueryForm(request.POST)
		if not f.is_valid():
			return render_to_response('postquery.html',{'form':f})
		else:
			q=Query()
			q.queryText=f.text
			q.userID=f.userID
			q.querytime=Timestamp
			q.save()
			qID=q.queryID
			return render_to_response('postquery.html',{'queryID':qID})
	return render_to_response('postquery.html',{'form':f})
