from Comment.models import Comment
from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):
	list_display = ('commentID_f', 'commentText', 'userID', 'isReported_f', 'reportingUserID', 'questionID', 'timeStamp' )
	
admin.site.register(Comment, CommentAdmin)
