from Ecodena.Attempt.models import *
from Ecodena.Question.models import *
from views import *

class CCompiler111(Compiler):

	def compile(self):
		import time, os

		print "\nStarting the Ecodena Judge Now...\n\n"

		#Following files are self defined based on filename
		usercode = self.attempt.solution_f
		inputdata = self.testcase.input_f
		outputdata = self.testcase.output_f
		
		#usercode = "a.c"
		#inputdata = "input"
		#outputdata= "answer"
		path = "static/storage/output"
		useroutput = "static/storage/output/userout"
		compileerrorfile="static/storage/output/error1"
		runerrorfile="static/storage/output/error2t"
		memoryfile = "static/storage/output/memory"
		
		errorReport = self.attempt.errorReportID_f
		errorReport.testCaseLevel_f = self.testcase.caseType_f
		

		compile_command = "gcc -o " +path + "/output " + usercode + " 2> "+compileerrorfile
		print "\nThe command we will run is: " + compile_command
		compile_return = os.system(compile_command)
		print "\nThe Compilation Result is: " + str(compile_return)

		print "\nCompilation results:"
		if(compile_return == 0):
			runMem = 0
			runtime = 0.0
			timeStart = 0.0
			timeEnd = 0.0
			print "\nThe code compiled successfully"
			run_command = "./" + path + "/output "+ inputdata  +" > "+useroutput+ " 2> "+runerrorfile
			print "\nNow we will run the code: " + run_command
			memCommand = "/usr/bin/time -f '%M' ./" + path + "/output " +inputdata+" > "+useroutput+" 2> "+memoryfile
			os.system(memCommand)
			temp = open(memoryfile)
			runMem = temp.read()
			print runMem
			runMem = runMem.splitlines()
			print runMem
			runMem = runMem[len(runMem) - 1]
			print runMem
			runMem = (int)(runMem)
			temp.close()
			print runMem
			timeStart = time.time()
			run_return = os.system(run_command)
			timeEnd = time.time()
		#	run_time = "/usr/bin/time ./a.out < input > temp"
			runtime = runtime + (timeEnd - timeStart)
			
			print "\nRun Program Return Value = " + str(run_return)
			if(run_return == 0):
				validate_command = "diff -Bw "+useroutput+" "+outputdata+" > /dev/null"
				timeStart = time.time()
				validate_output = os.system(validate_command)
				timeEnd = time.time()
		#		validate_time = "/usr/bin/time -f '%U' diff -Bw temp answer"
				runtime = runtime + (timeEnd - timeStart)
				print "\nThe Diff Return Value is: " + str(validate_output)
				print "The result is:"
				if(validate_output == 0):
					print "Correct answer."
					errorReport.errorType_f = 0
					errorReport.errorMessage_f = "Congratulations!\n Your code ran successfully and gave correct answer"
				else:
					print "Wrong answer."
					errorReport.errorType_f = 5
					errorReport.errorMessage_f = "Your code compiled successfully but it gave the wrong answer"
				print "Total Time Taken = " + str(runtime) + " seconds"
				print "Total Memory Taken = " + str(runMem) + " kB"
			else:
				print "Runtime Error"
				errorReport.errorType_f = 2
				errorReport.errorMessage_f = open(runerrorfile, "r").read()
			errorReport.timeRequirement_f = runtime
			errorReport.memory_f = runMem	
		else:
			print "The code did not compile successfully"
			print "For details regarding the error, see the file /error."
			errorReport.errorType_f = 1
			errorReport.errorMessage_f = open(compileerrorfile, "r").read()
			
			

				#print "Yuppy I am C Compiler with Version 1.1.1 and I just ran !"
		return errorReport
