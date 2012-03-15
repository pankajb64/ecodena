from Compiler.models import Language, CompilerVersion
from django.contrib import admin

class LanguageAdmin(admin.ModelAdmin):
	list_display   = ['languageName_f']


class CompilerVersionAdmin(admin.ModelAdmin):
	raw_id_fields = ['language_f']
	list_display = ( 'versionName_f', 'languageName')

admin.site.register(Language, LanguageAdmin)
admin.site.register(CompilerVersion, CompilerVersionAdmin)
