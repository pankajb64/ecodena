from threading import Lock
from celery.task.schedules import crontab
from datetime import timedelta
from celery.decorators import periodic_task
#import Ecodena.Attempt.models
from Ecodena.Attempt.models import Attempt, ErrorReport
from dictionary import compilers
from Ecodena.Question.models import *

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
#@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
#def test():    
 #   print "firing test task"
'''
@periodic_task(run_every=timedelta(seconds=1))
def gyo():    
    print "gyo"
    
'''
lock = Lock()
@periodic_task(run_every=timedelta(seconds=1))
def compile():
	
	lock.acquire()
	print "gyo"
	reports = ErrorReport.objects.filter(errorType_f = 6)
	
	if not reports:
		print "Nothing to do"
		return
		
	attempt = Attempt.objects.filter(errorReportID_f__in = reports)
	
	if not attempt:
		print "Nothing to do"
		return
	print "got attempt"
		
	attempt = attempt.order_by('timeOfSubmission_f')[0]
	
	question = attempt.questionID_f;
	
	version = attempt.compilerVersion
	
	compiler_ver_lang =  version.language.languageName + ' ' +version.versionName
	compiler = None
	if compiler_ver_lang in compilers:
		compiler = compilers[compiler_ver_lang]
		# do your main code
		#errorReportID = compiler(attempt.questionID, attempt)
	else: 
		print"Compiler not available " + compiler_ver_lang
		return None
	####################################################################
	questions = TestCase.objects.filter(questionID_f=question)
	if questions : 
		LowtestCasesList_f = questions.filter(caseType_f = 0)
		MedtestCasesList_f = questions.filter(caseType_f = 1)
		HightestCasesList_f = questions.filter(caseType_f = 2)
		print "running" + `compiler`
		errorReport = execute(attempt,question,compiler)
		if errorReport is not None:
			errorReport.save()
			attempt.errorReportID_f = errorReport
			attempt.save()
		else:
			print "Oops - Khali error report"					
	lock.release()

def execute(attempt,question,compiler):
	print "Running Execute"
	errorReport = None
	for testcase in question.LowtestCasesList_f:
		errorReport = compiler(question,attempt,testcase)
		if not errorReport.errorType_f == 0:
			break
	if errorReport and errorReport.errorType_f == 0:
		for testcase in question.MedtestCasesList_f:
			errorReport = compiler(question,attempt,testcase)
			if not errorReport.errorType_f == 0:
				break
		if errorReport and errorReport.errorType_f == 0:
			for testcase in question.HightestCasesList_f:
				errorReport = compiler(question,attempt,testcase)
				if not errorReport.errorType_f == 0:
					break
	return errorReport
