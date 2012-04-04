from multiprocessing import Lock
from celery.task.schedules import crontab
from datetime import timedelta
from celery.decorators import periodic_task
#import Ecodena.Attempt.models
from Ecodena.Attempt.models import Attempt, ErrorReport
from dictionary import compilers
from Ecodena.Question.models import *
import time

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
#@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
#def test():    
 #   print "firing test task"

lock = Lock()
'''
@periodic_task(run_every=timedelta(seconds=1))
def gyo():
	lock.acquire()    
	print "gyo"
	time.sleep(5)
	print "bye"
	#sleep(5)
	lock.release()
    

#lock = Lock()
'''

@periodic_task(run_every=timedelta(seconds=1))
def compile():
	pass
	
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
		question.LowtestCasesList_f = questions.filter(caseType_f = 0)
		question.MedtestCasesList_f = questions.filter(caseType_f = 1)
		question.HightestCasesList_f = questions.filter(caseType_f = 2)
		print "running" + `compiler`
		errorReport = execute(attempt,question,compiler)
		#errorReport.testCaseLevel_f=0
		if errorReport is not None:
			errorReport.save()
			attempt.errorReportID_f = errorReport
			if errorReport.errorType_f == 0:
				attempt.status_f = True
			attempt.save()
		else:
			print "Oops - Khali error report"					
	lock.release()

def execute(attempt,question,compiler):
	print "Running Execute"
	errorReport = None
	for testcase in question.LowtestCasesList_f:
		print "Low Test Case"
		errorReport = compiler(question,attempt,testcase)
		if not errorReport.errorType_f == 0:
			errorReport.errorMessage_f+="Your attempt failed on a Low Level Test Case"
			break
	errorReport.testCaseLevel_f=0		
	if errorReport and errorReport.errorType_f == 0:
		for testcase in question.MedtestCasesList_f:
			errorReport = compiler(question,attempt,testcase)
			if not errorReport.errorType_f == 0:
				errorReport.errorMessage_f+="Your attempt failed on a Medium Level Test Case"
				break
		errorReport.testCaseLevel_f=1		
		if errorReport and errorReport.errorType_f == 0:
			for testcase in question.HightestCasesList_f:
				errorReport = compiler(question,attempt,testcase)
				if not errorReport.errorType_f == 0:
					errorReport.errorMessage_f+="Your attempt failed on a High Level Test Case"
					break
			errorReport.testCaseLevel_f=2		
	return errorReport

