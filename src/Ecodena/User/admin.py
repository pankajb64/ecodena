#from User.models import User
from User.models import Programmer
from User.models import Profile
from django.contrib import admin

#admin.site.register(User)
admin.site.register(Programmer)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('profileID_f', 'dob_f', 'address_f', 'gender_f', 'userID_f', 'isProgrammer_f', 'isAdmin_f','isProblemSetter')
	
admin.site.register(Profile, ProfileAdmin)
