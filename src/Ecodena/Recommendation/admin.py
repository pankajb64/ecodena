from Recommendation.models import Recommendation
from Recommendation.models import Recommended
from django.contrib import admin


	
class RecommendedInline(admin.TabularInline):
	model = Recommendation.questionList_f.through
	
class RecommendationAdmin(admin.ModelAdmin):
	inlines = [RecommendedInline]

admin.site.register(Recommendation,RecommendationAdmin)
