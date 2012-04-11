from Ecodena.Attempt.models import *
from Ecodena.Question.models import *
from views import *
import subprocess
import time

'''
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException, "Timed out!"
        
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
   '''     		
class CppCompiler432(Compiler):

	def compile(self):
		import time, os, signal
		tleerror = 0
		class AlarmException(Exception):
			print Exception
			print("In AlarmException Class, your code has TLE error.")
			tleerror = 1
			pass	

		def alarmHandler(signum, frame):
			print "Your code has time out, sorry"
			raise AlarmException
		
	#	print "\nStarting the Ecodena Judge Now...\n\n"

		#Following files are self defined based on filename
		usercode = self.attempt.solution_f
		inputdata = self.testcase.input_f
		outputdata = self.testcase.output_f
		timelimit = self.question.timeLimit_f
		
		#usercode = "a.c"
		#inputdata = "input"
		#outputdata= "answer"
		path = "static/storage/output"
		useroutput = "static/storage/output/userout"
		compileerrorfile="static/storage/output/error1"
		runerrorfile="static/storage/output/error2t"
		memoryfile = "static/storage/output/memory"
		
		
		errorReport = self.attempt.errorReportID_f
		if not errorReport:
			errorReport = ErrorReport()
			
		errorReport.testCaseLevel_f = self.testcase.caseType_f
		
		#print "time limie is " + `timelimit`
		compile_command = "g++ -o " +path + "/output " + usercode + " 2> "+compileerrorfile
		#print "\nThe command we will run is: " + compile_command
		compile_return = os.system(compile_command)
		#print "\nThe Compilation Result is: " + str(compile_return)

		#print "\nCompilation results:"
		if(compile_return == 0):
			runMem = 0
			runtime = 0.0
			timeStart = 0.0
			timeEnd = 0.0
			tleerror = 0
			mleerror = 0
			message = ""
		#	print "\nThe code compiled successfully"
			run_command = "./" + path + "/output <"+ inputdata  +" > "+useroutput+ " 2> "+runerrorfile
		#	print "\nNow we will run the code: " + run_command
			memCommand = "ulimit -t " + str(int(timelimit)) + " ; /usr/bin/time -f '%M' ./" + path + "/output <" +inputdata+" > "+useroutput+" 2> "+memoryfile
		#	print memCommand
			#list = ["/usr/bin/time", "-f", "%M", "./" + path + "/output" , open(inputdata), open(useroutput), open(memoryfile)]
			#signal.signal(signal.SIGALRM, alarmHandler)
		#	print "1"
			#signal.alarm(int(timelimit))
		#	print "set alarm for " + `int(timelimit)`
			try:
		#		print "3"
				#time.sleep(10)
				return_value = os.system(memCommand)
		#		print "return value is " + `return_value`
				#proc = subprocess.Popen(list)
				#time.sleep((int(timelimit)))
				#pstatus = proc.poll()
				'''if pstatus is None:
					proc.kill()
					raise AlarmException'''
		#		print "4"
			except AlarmException:
		#		print "5"
		#		print("The Code Timed Out.")
				tleerror = 1
				print "6"
			except MemoryError:
		#		print "5"
		#		print("Memory Limit Exceeded.")
				mleerror = 1	
			signal.signal(signal.SIGALRM, signal.SIG_IGN)
		#	print "8"

			temp = open(memoryfile)
			runMem = temp.read()
		#	print runMem
			runMem = runMem.splitlines()
		#	print runMem
			ttemp = runMem[0]
			ttemp = ttemp.split(' ')
			errorcode = int(ttemp[len(ttemp) - 1])
			print errorcode
		#	print "The program returned a  error code " + str(errorcode) + "\nAre you happy now?"

			if not errorcode == 0:
		#		print errorcode
				if errorcode == 9:
					errorReport.errorType_f = 3
					errorReport.errorMessage_f = "Your code compiled successfully but it gave a time limit exceeded on execution\n"
					return errorReport
				else :
					errorReport.errorType_f = 2
		#			print errorcode
					message =   "Your code encountered an error while running. The returned signal was " + `errorcode` + ". Please search the internet for a list of all signals\n"	
					#print `errorcode` + message
#			return errorReport
			#runMem[0]
#			print message
			runMem = runMem[len(runMem) - 1]
#			print runMem
			runMem = (int)(runMem)
			temp.close()
#			print runMem
			timeStart = time.time()
			run_return = os.system(run_command)
			timeEnd = time.time()
		#	run_time = "/usr/bin/time ./a.out < input > temp"
			runtime = runtime + (timeEnd - timeStart)
			
#			print "\nRun Program Return Value = " + str(run_return)
			if(run_return == 0):
#				print useroutput
#				print outputdata
#				print open(useroutput).read()
#				print open(outputdata).read()
				validate_command = "diff -Bw "+useroutput+" "+outputdata+" > /dev/null"
				timeStart = time.time()
				validate_output = os.system(validate_command)
				timeEnd = time.time()
		#		validate_time = "/usr/bin/time -f '%U' diff -Bw temp answer"
				runtime = runtime + (timeEnd - timeStart)
#				print "\nThe Diff Return Value is: " + str(validate_output)
#				print "The result is:"
				if(validate_output == 0):
#					print "Correct answer."
					errorReport.errorType_f = 0
					errorReport.errorMessage_f = "Congratulations!\n Your code ran successfully and gave correct answer\n"
				else:
#					print "Wrong answer."
					errorReport.errorType_f = 5
					errorReport.errorMessage_f = "Your code compiled successfully but it gave the wrong answer\n"
#				print "Total Time Taken = " + str(runtime) + " seconds"
#				print "Total Memory Taken = " + str(runMem) + " kB"
			else:
#				print "Runtime Error"
				errorReport.errorType_f = 2
				errorReport.errorMessage_f = message + " " +  open(runerrorfile, "r").read() + "\n"
			errorReport.timeRequirement_f = runtime
			errorReport.memory_f = runMem	
		else:
#			print "The code did not compile successfully"
#			print "For details regarding the error, see the file /error."
			errorReport.errorType_f = 1
		#	print message 
			errorReport.errorMessage_f = open(compileerrorfile, "r").read() + "\n"
			
			
		print `errorReport.errorMessage_f`
				#print "Yuppy I am C Compiler with Version 1.1.1 and I just ran !"
		return errorReport
