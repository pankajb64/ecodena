from ProblemSetter.models import HasSet
from django.contrib import admin

class ProblemSetterAdmin(admin.ModelAdmin):
	list_display = ('questionID_f','userID_f')
admin.site.register(HasSet,ProblemSetterAdmin)	
