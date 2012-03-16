from Attempt.models import Attempt
from Attempt.models import ErrorReport
from django.contrib import admin

class AttemptAdmin(admin.ModelAdmin):
	list_display = ('attemptID_f', 'questionID_f', 'userID', 'solution_f', 'errorReportID', 'status_f', 'timeOfSubmission' )
	
admin.site.register(Attempt, AttemptAdmin)

class ErrorReportAdmin(admin.ModelAdmin):
	list_display = ('errorReportID_f', 'timeRequirement_f', 'memory_f', 'errorType_f', 'errorMessage_f', 'testCaseLevel_f')

admin.site.register(ErrorReport, ErrorReportAdmin)
