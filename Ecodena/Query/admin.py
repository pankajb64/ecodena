from Query.models import Query
from django.contrib import admin

class QueryAdmin(admin.ModelAdmin):
	list_display = ( 'queryID', 'queryText', 'userID', 'queryTime', 'solution', 'adminID', 'replyTime')
	
admin.site.register(Query, QueryAdmin)
