from celery.task.schedules import crontab
from datetime import timedelta
from celery.decorators import periodic_task
#import Ecodena.Attempt.models
from Ecodena.Attempt.models import Attempt, ErrorReport
from dictionary import compilers

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
#@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
#def test():    
 #   print "firing test task"
'''
@periodic_task(run_every=timedelta(seconds=1))
def gyo():    
    print "gyo"
    
'''
  
@periodic_task(run_every=timedelta(seconds=1))
def compile():
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
	#retrieve all three test case lists for question from Database
	
	version = attempt.compilerVersion
	
	compiler_ver_lang =  version.language.languageName + ' ' +version.versionName
	
	if compiler_ver_lang in compilers:
		compiler = compilers[compiler_ver_lang]
		# do your main code
		errorReportID = compiler(attempt.questionID, attempt)
	else: 
		print"Compiler not available " + compiler_ver_lang
	

