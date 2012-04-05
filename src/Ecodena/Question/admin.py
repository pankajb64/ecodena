from Question.models import Question
from Question.models import Type
from Question.models import Level
from Question.models import TestCase
from django.contrib import admin

class TypeInline(admin.StackedInline):
	model = Type
	extra = 2
class LevelInline(admin.StackedInline):
	model = Level
	extra =2

class QuestionAdmin(admin.ModelAdmin):
	inlines1 = [TypeInline]
	inlines2 = [LevelInline]
	list_display = ('questionID_f', 'questionTitle', 'level_f',  'type_f', 'timeLimit_f')
	#questionText_f.allow_tags = True


admin.site.register(Question, QuestionAdmin)
admin.site.register(Type)
admin.site.register(Level)
admin.site.register(TestCase)
