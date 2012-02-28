from django.db import models

# Create your models here.

class Question(models.Model)
	questionID = models.AutoField(primary_key=True)
	questionText = models.TextField("Problem Statement", null=False)
	level = models.ForeignKey(Level, verbose_name="Question Level", null=False)
	type = models.ForeignKey(Type, verbose_name="Type of Question", null=False)

class Level(models.Model)
	levelID = models.AutoField(primary_key=True)
	levelName = models.CharField("Level Name", max_length = 20 , null = False)
	
class Type(models.Model)
	typeID = models.AutoField(primary_key=True)
	typeName = models.CharField("Type Name" , max_length = 30 , null = False)

class TestCases(models.Model)
	caseID = models.AutoField(primary_keys=True)
	questionID = models.ForeignKey(Question , verbose_name="Question ID", null=False)
	CASE_TYPE = ((0, 'Low'), (1, 'Medium'), (2, 'High'))
	caseType = models.SmallIntegerField(choices=CASE_TYPE, verbose_name="Type of Case")
	input = models.TextField("Input")	
	output = models.TextField("Output")
	
