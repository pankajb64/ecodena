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

import signal

class AlarmException(Exception):
	print Exception
	print("In AlarmException Class, your code has TLE error.")
	pass

def alarmHandler(signum, frame):
	print "Your code has time out, sorry"
	raise AlarmException
	
	
@periodic_task(run_every=timedelta(seconds=1))
def gyo():
	pass
	'''
	try :
		lock.acquire()
		signal.signal(signal.SIGALRM, alarmHandler)
		print "1"
		x = signal.alarm(3)
		print "x"
		    
		print "gyo"
		
		time.sleep(5)
		print "bye"
		#sleep(5)
	finally:
		lock.release()
    '''

#lock = Lock()


@periodic_task(run_every=timedelta(seconds=10))
def compile():
	#print "x"
	#pass
	
	
	try:
		lock.acquire()
		#print "gyo"
		reports = ErrorReport.objects.filter(errorType_f = 6)
		
		if not reports:
		#	print "Nothing to do"
			return
			
		attempt = Attempt.objects.filter(errorReportID_f__in = reports)
		
		if not attempt:
		#	print "Nothing to do"
			return
		#print "got attempt"
			
		attempt = attempt.order_by('timeOfSubmission_f')[0]
		#print "1"
		question = attempt.questionID_f;
		
		version = attempt.compilerVersion
		#print "2"
		compiler_ver_lang =  version.language.languageName + ' ' +version.versionName
		compiler = None
		if compiler_ver_lang in compilers:
			compiler = compilers[compiler_ver_lang]
			# do your main code
			#errorReportID = compiler(attempt.questionID, attempt)
		else: 
		#	print"Compiler not available " + compiler_ver_lang
			return None
		####################################################################
		#print "question is " + `question.questionTitle_f`
		test_cases = TestCase.objects.filter(questionID_f=question)
		#print "running" + `compiler` 
		if test_cases : 
		#	print "question"
			question.LowtestCasesList_f = test_cases.filter(caseType_f = 0)
			question.MedtestCasesList_f = test_cases.filter(caseType_f = 1)
			question.HightestCasesList_f = test_cases.filter(caseType_f = 2)
			
			errorReport = execute(attempt,question,compiler)
			#errorReport.testCaseLevel_f=0
			if errorReport is not None:
				errorReport.save()
				attempt.errorReportID_f = errorReport
				if errorReport.errorType_f == 0:
					attempt.status_f = True
				attempt.save()
			else:
				pass
		#		print "Oops - Khali error report"
		else:
			er = ErrorReport()
			er.errorType_f=0
			er.errorMessage_f="There were no test cases associated with the question, so your answer is marked as correct\n"
			er.save()
			attempt.errorReportID_f = er
			attempt.status_f = True
			attempt.save()		
	finally:					
		lock.release()

def execute(attempt,question,compiler):
	#print "Running Execute"
	errorReport = None
	for testcase in question.LowtestCasesList_f:
	#	print "Low Test Case"
		errorReport = compiler(question,attempt,testcase)
		if not errorReport.errorType_f == 0:
			errorReport.errorMessage_f+="Your Solution Failed for low level test cases. Probably something is wrong with your basic algorithm or your code syntax.\n"
			break
	errorReport.testCaseLevel_f=0		
	if errorReport and errorReport.errorType_f == 0:
		for testcase in question.MedtestCasesList_f:
			errorReport = compiler(question,attempt,testcase)
			if not errorReport.errorType_f == 0:
				errorReport.errorMessage_f+="Your solution failed for medium level test cases. Probabaly something is wrong while checking the corner cases. \nIn cases of off-by-one errors make sure to check your array indices and loop iterator variables\n"
				break
		errorReport.testCaseLevel_f=1		
		if errorReport and errorReport.errorType_f == 0:
			for testcase in question.HightestCasesList_f:
				errorReport = compiler(question,attempt,testcase)
				if not errorReport.errorType_f == 0:
					errorReport.errorMessage_f+="Your solution failed for high level test cases. Probably something is wrong with the performance of your program.\n Remember, in most cases, your algorithm needs to be optimal to clear high level test cases"
					break
			errorReport.testCaseLevel_f=2
	if errorReport.errorType_f == 1:
		errorReport.errorMessage_f+="Your solution failed to compile successfully.\n"
	if errorReport.errorType_f == 2:
		errorReport.errorMessage_f+="Your solution generated a run time error.\n It could be a Segmentation fault or a fatal error because of which your program is aborting unexpectedly.\n"
	if errorReport.errorType_f == 3:
		errorReport.errorMessage_f+="Your solution failed to compile within given Time Limit because your program is too slow.\nThe time limits are all attainable, so you will just need to come up with a way of making your algorithm faster.\n"
	if errorReport.errorType_f == 4:
		errorReport.errorMessage_f+="Your solution exceeded the given memory limit. This type of error is sometimes generated if you use too much memory. Check for arrays that are too large, or other elements that could grow to a size too large to fit in memory.\n"
	if errorReport.errorType_f == 5:
		errorReport.errorMessage_f+="Your program is not printing out the correct answer. You will just have to debug your program very carefully! Make sure your program is conforming exactly to the output format required, and not printing out unnecessary information.\n"				
				
	return errorReport
