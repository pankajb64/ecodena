from Contest.models import Contest 
from Contest.models import ContestQuestion
from Contest.models import ContestParticipants
from django.contrib import admin
class ContestAdmin(admin.ModelAdmin):
	list_display=('contestID_f','contestName_f','contestPwd_f','termsCond_f','adminID_f','contestToDate_f','contestFromDate_f','contestFromTime_f','contestToTime_f')

class ContestQuestionAdmin(admin.ModelAdmin):
	list_display=('contestID_f','questionID_f')

class ContestParticipantsAdmin(admin.ModelAdmin):
	list_display=('contestID_f','userID_f')	

admin.site.register(Contest,ContestAdmin)
admin.site.register(ContestQuestion,ContestQuestionAdmin)
admin.site.register(ContestParticipants,ContestParticipantsAdmin)		
