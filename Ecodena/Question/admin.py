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

admin.site.register(Question)
admin.site.register(Type)
admin.site.register(Level)
