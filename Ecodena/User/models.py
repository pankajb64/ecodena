from django.db import models

# Create your models here.

class User(models.Model)
	userID = models.AutoField(primary_key=True)
	userName = models.CharField("User name", max_length=30, null=False)
	password = models.CharField("Password", max_length=12, null=False)
	isProgrammer = models.BooleanField("Is a Programmer", default=True)
	isAdmin = models.BooleanField("Is Administrator", default=False)
