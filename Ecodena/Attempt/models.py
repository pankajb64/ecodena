from django.db import models
from Ecodena.Question import Question
from Ecodena.User import User

# Create your models here.

class Attempt(models.Model)
	attemptID = models.AutoField(primary_key=True)
	questionID = models.ForeignKey(Question, verbose_name="Question ID", null=False)
	userID = models.ForeignKey(User, verbose_name="User ID", null=False)
	solution = models.TextField("Solution uploaded by the User", null=False)
	errorReport = models.TextField("Error Report for the Solution", null=False)
	status = models.BooleanField("Status of attempt - true = right, false = wrong")
	timeOfSubmission = models.DateTimeField("Time of Submission", null=False)
